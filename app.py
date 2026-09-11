import streamlit as st
import pandas as pd
from datetime import datetime
import time
import os
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="IronTracker", page_icon="🏋️", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 5rem; padding-left: 0.8rem; padding-right: 0.8rem; }
    .stButton>button { border-radius: 12px; font-weight: 700; width: 100%; }
    </style>
""", unsafe_allow_html=True)

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# -------------------------------------------------------------
# 1. CONEXÃO EM CACHE (EVITA ERRO 429)
# -------------------------------------------------------------
@st.cache_resource
def obter_cliente_gspread():
    creds_dict = dict(st.secrets["gcp_service_account"])
    credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
    return gspread.authorize(credentials)

@st.cache_data(ttl=600, show_spinner=False)
def carregar_dados_planilha():
    client = obter_cliente_gspread()
    sheet_id = str(st.secrets["SHEET_ID"]).strip()
    planilha = client.open_by_key(sheet_id)
    titulos_abas = [w.title for w in planilha.worksheets()]
    
    # Busca aba de exercícios
    dados_ex = []
    for nome in ["Exercicios", "Exercícios", "exercicios", "Sheet1", "Página1", titulos_abas[0]]:
        if nome in titulos_abas:
            aba_ex = planilha.worksheet(nome)
            dados_ex = aba_ex.get_all_records()
            break

    # Busca aba de histórico
    dados_hist = []
    aba_hist_nome = None
    for nome in ["Registro_Treinos", "Registro de Treinos", "Historico", "historico"]:
        if nome in titulos_abas:
            aba_hist_nome = nome
            aba_h = planilha.worksheet(nome)
            dados_hist = aba_h.get_all_records()
            break

    return pd.DataFrame(dados_ex), pd.DataFrame(dados_hist), aba_hist_nome

# Executa com fallback suave
msg_status = None
try:
    if "gcp_service_account" in st.secrets and "SHEET_ID" in st.secrets:
        df_exercicios, df_historico, nome_aba_hist = carregar_dados_planilha()
    else:
        df_exercicios, df_historico, nome_aba_hist = pd.DataFrame(), pd.DataFrame(), None
        msg_status = "Secrets 'SHEET_ID' ou 'gcp_service_account' ausentes."
except Exception as e:
    df_exercicios, df_historico, nome_aba_hist = pd.DataFrame(), pd.DataFrame(), None
    msg_status = f"Limite temporário atingido no Google. Aguarde 1 minuto. Detalhe: {e}"

# -------------------------------------------------------------
# 2. FUNÇÃO INTELIGENTE DE IMAGEM
# -------------------------------------------------------------
def exibir_imagem_exercicio(caminho_ou_url):
    if not caminho_ou_url:
        st.caption("📷 *Sem foto cadastrada*")
        return
        
    caminho_str = str(caminho_ou_url).strip()
    
    if caminho_str.startswith("http://") or caminho_str.startswith("https://"):
        st.image(caminho_str, use_container_width=True)
        return

    nome_arquivo = os.path.basename(caminho_str)
    pastas_para_testar = [
        "Imagens", "imagens", ".",
        os.path.join(os.path.dirname(__file__), "Imagens"),
        os.path.join(os.path.dirname(__file__), "imagens")
    ]
    
    achou = False
    for pasta in pastas_para_testar:
        possivel_caminho = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(possivel_caminho):
            st.image(possivel_caminho, use_container_width=True)
            achou = True
            break
            
    if not achou:
        st.caption(f"📷 *Arquivo '{nome_arquivo}' não encontrado na pasta Imagens/*")

# -------------------------------------------------------------
# 3. INTERFACE PRINCIPAL
# -------------------------------------------------------------
st.title("🏋️ IronTracker")
st.caption("Memória de Cargas & Catálogo de Treinos")

if msg_status:
    st.warning(msg_status)

# Cronômetro de descanso
with st.expander("⏱️ Cronômetro de Descanso", expanded=False):
    c1, c2, c3 = st.columns(3)
    def contar_tempo(segundos):
        barra = st.progress(100)
        texto = st.empty()
        for s in range(segundos, 0, -1):
            barra.progress(int((s / segundos) * 100))
            texto.metric("Tempo Restante", f"{s}s")
            time.sleep(1)
        st.success("Hora da próxima série!")

    if c1.button("60s"): contar_tempo(60)
    if c2.button("90s"): contar_tempo(90)
    if c3.button("120s"): contar_tempo(120)

tab_treino, tab_historico, tab_nutricao = st.tabs(["Treinos", "Histórico", "Nutrição"])

with tab_treino:
    divisao = st.segmented_control(
        "Divisão do Dia:",
        options=["push", "pull", "legs", "outros"],
        format_func=lambda x: {"push": "Push (A)", "pull": "Pull (B)", "legs": "Legs (C)", "outros": "Core/Func"}[x],
        default="push"
    )

    coluna_div = None
    if not df_exercicios.empty:
        for c in ["Divisao", "divisao", "Categoria", "categoria"]:
            if c in df_exercicios.columns:
                coluna_div = c
                break

    if not df_exercicios.empty and coluna_div:
        filtro = df_exercicios[df_exercicios[coluna_div].astype(str).str.lower().str.strip() == divisao]
        
        if filtro.empty:
            st.info(f"Nenhum exercício cadastrado para a divisão '{divisao}'.")

        for _, row in filtro.iterrows():
            nome_ex = row.get("Nome_Exercicio") or row.get("Exercicio") or row.get("Nome") or "Exercício"
            ex_id = str(row.get("ID", nome_ex))
            img_ref = row.get("URL_ou_Caminho_Imagem") or row.get("Imagem") or row.get("URL_Imagem") or ""

            with st.container(border=True):
                col_texto, col_foto = st.columns([2.2, 1])

                with col_texto:
                    st.markdown(f"### {nome_ex}")
                    musculo = row.get("Musculo_Alvo") or row.get("Musculo") or ""
                    reps_sug = row.get("Series_Reps") or row.get("Reps") or ""
                    st.caption(f"🎯 {musculo} • {reps_sug}")

                with col_foto:
                    exibir_imagem_exercicio(img_ref)

                # Última carga salva
                if not df_historico.empty and "Exercicio" in df_historico.columns:
                    registros_anteriores = df_historico[df_historico["Exercicio"] == nome_ex]
                    if not registros_anteriores.empty:
                        ultimo = registros_anteriores.iloc[-1]
                        st.info(f"Último: **{ultimo.get('Carga_kg', 0)} kg × {ultimo.get('Reps', 0)} reps** em {ultimo.get('Data', '')}")
                    else:
                        st.caption("Nenhum registro anterior.")
                else:
                    st.caption("Sem histórico anterior.")

                # Inputs
                cc1, cc2, cc3 = st.columns([1.2, 1.2, 1.4])
                carga = cc1.number_input("Carga (kg)", min_value=0.0, step=0.5, key=f"c_{ex_id}")
                reps = cc2.number_input("Reps", min_value=1, step=1, value=10, key=f"r_{ex_id}")

                if cc3.button("Salvar Série", key=f"btn_{ex_id}"):
                    if nome_aba_hist:
                        client = obter_cliente_gspread()
                        sheet_id = str(st.secrets["SHEET_ID"]).strip()
                        pl = client.open_by_key(sheet_id)
                        aba_target = pl.worksheet(nome_aba_hist)
                        
                        nova_linha = [
                            datetime.now().strftime("%Y-%m-%d"),
                            datetime.now().strftime("%H:%M"),
                            divisao,
                            nome_ex,
                            1,
                            carga,
                            reps,
                            carga * reps,
                            "Salvo via App"
                        ]
                        aba_target.append_row(nova_linha)
                        st.cache_data.clear()  # Limpa o cache para recarregar o novo histórico
                        st.success("Série salva com sucesso!")
                        st.rerun()
                    else:
                        st.error("Aba de histórico não encontrada na planilha.")

                with st.expander("Instruções de Postura"):
                    st.write(row.get("Instrucoes_Postura", "Execute de forma controlada."))

        if st.button("🏁 FINALIZAR TREINO DO DIA", type="primary"):
            st.balloons()
            st.success("Treino finalizado com sucesso!")
    elif df_exercicios.empty and not msg_status:
        st.warning("Carregando exercícios...")

with tab_historico:
    st.subheader("Histórico de Séries")
    if not df_historico.empty:
        st.dataframe(df_historico, use_container_width=True)
    else:
        st.info("Nenhuma série salva na aba de histórico.")

with tab_nutricao:
    st.subheader("Meta Nutricional (~3.000 kcal)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Proteína", "160g")
    m2.metric("Carboidrato", "400g")
    m3.metric("Gordura", "85g")
