import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Configuração da página para mobile
st.set_page_config(
    page_title="IronTracker",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual moderno para smartphone
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 5rem; padding-left: 1rem; padding-right: 1rem; }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 1. CONEXÃO COM A PLANILHA
# -------------------------------------------------------------
# Substitua pelo ID da sua planilha do Google Sheets ou use local 'base_treino_completo.xlsx'
SHEET_ID = "COLE_O_ID_DA_SUA_PLANILHA_AQUI"
CSV_EXERCICIOS_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Exercicios"

@st.cache_data(ttl=60)
def carregar_exercicios():
    try:
        df = pd.read_csv(CSV_EXERCICIOS_URL)
        return df
    except Exception:
        # Fallback caso esteja rodando offline com o arquivo excel local
        try:
            return pd.read_excel("base_treino_completo.xlsx", sheet_name="Exercicios")
        except Exception:
            return pd.DataFrame()

# Inicializa histórico em sessão local se não estiver conectado a uma API de gravação
if "historico_treinos" not in st.session_state:
    try:
        df_hist = pd.read_excel("base_treino_completo.xlsx", sheet_name="Registro_Treinos")
        st.session_state.historico_treinos = df_hist
    except Exception:
        st.session_state.historico_treinos = pd.DataFrame(
            columns=["Data", "Hora", "Divisao", "Exercicio", "Serie", "Carga_kg", "Reps", "Volume_kg", "Observacoes"]
        )

df_exercicios = carregar_exercicios()

# -------------------------------------------------------------
# 2. TOPO & TIMER DE DESCANSO
# -------------------------------------------------------------
st.title("🏋️ IronTracker")
st.caption("Memória de Cargas & Guia Visual de Treino")

with st.expander("⏱️ Cronômetro de Descanso", expanded=False):
    col_t1, col_t2, col_t3 = st.columns(3)
    if col_t1.button("60s"):
        barra = st.progress(100)
        for i in range(60, 0, -1):
            barra.progress(int((i / 60) * 100), text=f"Descanso: {i}s restantes")
            time.sleep(1)
        st.success("Hora da próxima série!")
    if col_t2.button("90s"):
        barra = st.progress(100)
        for i in range(90, 0, -1):
            barra.progress(int((i / 90) * 100), text=f"Descanso: {i}s restantes")
            time.sleep(1)
        st.success("Hora da próxima série!")
    if col_t3.button("120s"):
        barra = st.progress(100)
        for i in range(120, 0, -1):
            barra.progress(int((i / 120) * 100), text=f"Descanso: {i}s restantes")
            time.sleep(1)
        st.success("Hora da próxima série!")

# -------------------------------------------------------------
# 3. ABAS: TREINOS vs HISTÓRICO
# -------------------------------------------------------------
tab_treino, tab_historico, tab_nutricao = st.tabs(["Treino", "Histórico", "Nutrição"])

with tab_treino:
    divisao = st.segmented_control(
        "Divisão do Dia",
        options=["push", "pull", "legs", "outros"],
        format_func=lambda x: {"push": "Push (A)", "pull": "Pull (B)", "legs": "Legs (C)", "outros": "Core/Func"}[x],
        default="push"
    )

    if not df_exercicios.empty and "Divisao" in df_exercicios.columns:
        df_filtrado = df_exercicios[df_exercicios["Divisao"].str.lower() == divisao]
        
        for _, ex in df_filtrado.iterrows():
            nome_ex = ex["Nome_Exercicio"]
            
            with st.container(border=True):
                col_info, col_img = st.columns([2.2, 1])
                
                with col_info:
                    st.subheader(nome_ex)
                    st.caption(f"🎯 {ex['Musculo_Alvo']} • {ex['Series_Reps']}")
                
                with col_img:
                    img_path = str(ex.get("URL_ou_Caminho_Imagem", ""))
                    if img_path.startswith("http"):
                        st.image(img_path, use_container_width=True)
                    elif img_path:
                        try:
                            st.image(img_path, use_container_width=True)
                        except Exception:
                            st.markdown("🖼️ *(sem foto)*")

                # Memória da última carga
                hist = st.session_state.historico_treinos
                ultimo_reg = hist[hist["Exercicio"] == nome_ex]
                if not ultimo_reg.empty:
                    ult_linha = ultimo_reg.iloc[-1]
                    st.info(f"Último registro: **{ult_linha['Carga_kg']} kg × {ult_linha['Reps']} reps** em {ult_linha['Data']}")
                else:
                    st.caption("Nenhum registro anterior.")

                # Inputs de Carga e Repetições
                col_c, col_r, col_save = st.columns([1.2, 1.2, 1.4])
                carga = col_c.number_input("Carga (kg)", min_value=0.0, step=0.5, key=f"c_{ex['ID']}")
                reps = col_r.number_input("Reps", min_value=1, step=1, value=10, key=f"r_{ex['ID']}")
                
                if col_save.button("Salvar Série", key=f"btn_{ex['ID']}"):
                    novo_log = {
                        "Data": datetime.now().strftime("%Y-%m-%d"),
                        "Hora": datetime.now().strftime("%H:%M"),
                        "Divisao": divisao,
                        "Exercicio": nome_ex,
                        "Serie": len(ultimo_reg) + 1,
                        "Carga_kg": carga,
                        "Reps": reps,
                        "Volume_kg": carga * reps,
                        "Observacoes": "Gravado via app"
                    }
                    st.session_state.historico_treinos = pd.concat(
                        [st.session_state.historico_treinos, pd.DataFrame([novo_log])],
                        ignore_index=True
                    )
                    st.success("Série salva!")
                    st.rerun()

                with st.expander("Instruções de Postura"):
                    st.write(ex.get("Instrucoes_Postura", "Execute de forma controlada."))

        if st.button("🏁 FINALIZAR TREINO DO DIA", type="primary"):
            st.balloons()
            st.success("Treino concluído com sucesso! Suas cargas estão salvas.")
    else:
        st.warning("Carregando exercícios da planilha...")

with tab_historico:
    st.subheader("Histórico de Séries Realizadas")
    if not st.session_state.historico_treinos.empty:
        st.dataframe(st.session_state.historico_treinos, use_container_width=True)
        # Botão para baixar a planilha atualizada
        csv_data = st.session_state.historico_treinos.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Baixar Histórico em CSV",
            data=csv_data,
            file_name=f"historico_treino_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.write("Nenhuma série gravada ainda.")

with tab_nutricao:
    st.subheader("Meta Nutricional Diária (~3.000 kcal)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Proteína", "160g", "~640 kcal")
    c2.metric("Carboidratos", "400g", "~1.600 kcal")
    c3.metric("Gorduras", "85g", "~780 kcal")
    
    st.markdown("""
    **Guia Rápido da Mão:**
    * 🖐️ **Palma da mão:** ~150g de carne/frango/peixe
    * ✊ **Punho fechado:** ~100g de arroz ou batata
    * 👍 **Polegar:** ~15g de azeite ou pasta de amendoim
    """)
