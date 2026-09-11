import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import os
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# -------------------------------------------------------------
st.set_page_config(
    page_title="IronTracker",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# 2. ESTILIZAÇÃO VISUAL NATIVA MOBILE (UI REFINADA)
# -------------------------------------------------------------
st.markdown("""
    <style>
    /* Reset e fundo escuro moderno */
    .stApp {
        background-color: #030712;
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Trava de largura para mobile */
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 5rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 480px !important;
        margin: 0 auto;
    }

    /* Cards de Exercícios */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 18px !important;
        padding: 0.9rem !important;
        box-shadow: 0 4px 15px -3px rgba(0, 0, 0, 0.4) !important;
        margin-bottom: 0.75rem !important;
    }

    /* Botões táteis com feedback */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 0.5rem 0.8rem !important;
        transition: transform 0.1s ease, background-color 0.2s ease !important;
    }
    .stButton > button:active {
        transform: scale(0.96) !important;
    }

    /* Imagens com cantos arredondados */
    img {
        border-radius: 12px !important;
        object-fit: cover !important;
    }

    /* Inputs numéricos limpos */
    div[data-baseweb="input"] {
        border-radius: 10px !important;
        background-color: #020617 !important;
        border: 1px solid #334155 !important;
    }

    /* Ocultar barra superior padrão do Streamlit */
    #MainMenu, header, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# -------------------------------------------------------------
# 3. CONEXÃO COM GOOGLE SHEETS COM CACHE (SEM ERRO 429)
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
    titulos = [w.title for w in planilha.worksheets()]
    
    # Busca aba Exercicios
    dados_ex = []
    for nome in ["Exercicios", "Exercícios", "exercicios", "Sheet1", "Página1", titulos[0]]:
        if nome in titulos:
            aba_ex = planilha.worksheet(nome)
            dados_ex = aba_ex.get_all_records()
            break

    # Busca aba Registro_Treinos
    dados_hist = []
    aba_hist_nome = None
    for nome in ["Registro_Treinos", "Registro de Treinos", "Historico", "historico"]:
        if nome in titulos:
            aba_hist_nome = nome
            aba_h = planilha.worksheet(nome)
            dados_hist = aba_h.get_all_records()
            break

    return pd.DataFrame(dados_ex), pd.DataFrame(dados_hist), aba_hist_nome

msg_status = None
try:
    if "gcp_service_account" in st.secrets and "SHEET_ID" in st.secrets:
        df_exercicios, df_historico, nome_aba_hist = carregar_dados_planilha()
    else:
        df_exercicios, df_historico, nome_aba_hist = pd.DataFrame(), pd.DataFrame(), None
        msg_status = "Configure os Secrets com 'SHEET_ID' e 'gcp_service_account'."
except Exception as e:
    df_exercicios, df_historico, nome_aba_hist = pd.DataFrame(), pd.DataFrame(), None
    msg_status = f"Aguardando conexão com Google Sheets: {e}"

# -------------------------------------------------------------
# 4. RENDERIZADOR DE IMAGENS (LOCAL OU URL)
# -------------------------------------------------------------
def renderizar_imagem(caminho_ou_url):
    if not caminho_ou_url:
        st.caption("📷 *Sem foto*")
        return
        
    caminho_str = str(caminho_ou_url).strip()
    if caminho_str.startswith("http://") or caminho_str.startswith("https://"):
        st.image(caminho_str, use_container_width=True)
        return

    nome_arquivo = os.path.basename(caminho_str)
    pastas = [
        "Imagens", "imagens", ".",
        os.path.join(os.path.dirname(__file__), "Imagens"),
        os.path.join(os.path.dirname(__file__), "imagens")
    ]
    
    for pasta in pastas:
        possivel = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(possivel):
            st.image(possivel, use_container_width=True)
            return
            
    st.caption(f"📷 *{nome_arquivo}*")

# -------------------------------------------------------------
# 5. HEADER & CRONÔMETRO COM ALARME EM JAVASCRIPT NATIVO
# -------------------------------------------------------------
st.title("🏋️ IronTracker")
st.caption("Memória de Cargas & Catálogo de Treinos")

if msg_status:
    st.warning(msg_status)

# Componente HTML/JS: Roda no navegador do celular, sem travar o app e com bip sonoro garantido
components.html("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #f8fafc;
  }
  .timer-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }
  .display-box {
    display: flex;
    flex-direction: column;
  }
  .title {
    font-size: 10px;
    text-transform: uppercase;
    color: #94a3b8;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .time {
    font-size: 32px;
    font-weight: 900;
    font-family: monospace;
    color: #38bdf8;
    line-height: 1.1;
  }
  .actions {
    display: flex;
    gap: 6px;
  }
  button {
    background: #1e293b;
    color: #f8fafc;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 8px 12px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: background 0.2s, transform 0.1s;
  }
  button:active {
    transform: scale(0.94);
    background: #0284c7;
  }
  .btn-stop {
    background: #450a0a;
    color: #f87171;
    border-color: #7f1d1d;
  }
  .btn-stop:active {
    background: #991b1b;
  }
</style>
</head>
<body>
<div class="timer-card">
  <div class="display-box">
    <span class="title">Descanso</span>
    <span class="time" id="clock">00:00</span>
  </div>
  <div class="actions">
    <button onclick="startTimer(60)">60s</button>
    <button onclick="startTimer(90)">90s</button>
    <button onclick="startTimer(120)">120s</button>
    <button class="btn-stop" onclick="stopTimer()">Parar</button>
  </div>
</div>

<script>
  let timerTarget = null;
  let timerInterval = null;
  let audioCtx = null;

  function initAudio() {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function playAlarm() {
    try {
      initAudio();
      const now = audioCtx.currentTime;

      // Beep 1
      const osc1 = audioCtx.createOscillator();
      const gain1 = audioCtx.createGain();
      osc1.frequency.setValueAtTime(880, now);
      gain1.gain.setValueAtTime(0.3, now);
      gain1.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
      osc1.connect(gain1);
      gain1.connect(audioCtx.destination);
      osc1.start(now);
      osc1.stop(now + 0.25);

      // Beep 2 (agudo)
      const osc2 = audioCtx.createOscillator();
      const gain2 = audioCtx.createGain();
      osc2.frequency.setValueAtTime(1174, now + 0.3);
      gain2.gain.setValueAtTime(0.4, now + 0.3);
      gain2.gain.exponentialRampToValueAtTime(0.01, now + 0.7);
      osc2.connect(gain2);
      gain2.connect(audioCtx.destination);
      osc2.start(now + 0.3);
      osc2.stop(now + 0.7);

      if (navigator.vibrate) {
        navigator.vibrate([200, 100, 200, 100, 300]);
      }
    } catch (e) {
      console.log("Erro de áudio:", e);
    }
  }

  function startTimer(seconds) {
    initAudio();
    clearInterval(timerInterval);
    timerTarget = Date.now() + (seconds * 1000);
    updateDisplay();
    timerInterval = setInterval(updateDisplay, 250);
  }

  function stopTimer() {
    clearInterval(timerInterval);
    timerTarget = null;
    document.getElementById("clock").innerText = "00:00";
  }

  function updateDisplay() {
    if (!timerTarget) return;
    const diff = timerTarget - Date.now();
    if (diff <= 0) {
      stopTimer();
      playAlarm();
      return;
    }
    const totalSec = Math.ceil(diff / 1000);
    const m = Math.floor(totalSec / 60);
    const s = totalSec % 60;
    document.getElementById("clock").innerText = 
      String(m).padStart(2, '0') + ":" + String(s).padStart(2, '0');
  }
</script>
</body>
</html>
""", height=90)

# -------------------------------------------------------------
# 6. ABAS DO APLICATIVO
# -------------------------------------------------------------
tab_treino, tab_historico, tab_nutricao = st.tabs(["Treinos", "Histórico", "Nutrição"])

with tab_treino:
    divisao = st.segmented_control(
        "Divisão do Treino",
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
            st.info(f"Nenhum exercício encontrado para '{divisao}'.")

        for _, row in filtro.iterrows():
            nome_ex = row.get("Nome_Exercicio") or row.get("Exercicio") or row.get("Nome") or "Exercício"
            ex_id = str(row.get("ID", nome_ex))
            img_ref = row.get("URL_ou_Caminho_Imagem") or row.get("Imagem") or row.get("URL_Imagem") or ""

            with st.container(border=True):
                col_texto, col_foto = st.columns([2.2, 1])

                with col_texto:
                    st.markdown(f"**{nome_ex}**")
                    musculo = row.get("Musculo_Alvo") or row.get("Musculo") or ""
                    reps_sug = row.get("Series_Reps") or row.get("Reps") or ""
                    st.caption(f"🎯 {musculo} • {reps_sug}")

                with col_foto:
                    renderizar_imagem(img_ref)

                # Busca o último registro de treino salvo
                if not df_historico.empty and "Exercicio" in df_historico.columns:
                    registros_anteriores = df_historico[df_historico["Exercicio"] == nome_ex]
                    if not registros_anteriores.empty:
                        ultimo = registros_anteriores.iloc[-1]
                        st.info(f"Último: **{ultimo.get('Carga_kg', 0)} kg × {ultimo.get('Reps', 0)} reps** em {ultimo.get('Data', '')}")
                    else:
                        st.caption("Nenhum registro anterior.")
                else:
                    st.caption("Sem histórico anterior.")

                # Inputs de Carga e Reps
                cc1, cc2, cc3 = st.columns([1.2, 1.2, 1.4])
                carga = cc1.number_input("Carga (kg)", min_value=0.0, step=0.5, key=f"c_{ex_id}")
                reps = cc2.number_input("Reps", min_value=1, step=1, value=10, key=f"r_{ex_id}")

                if cc3.button("Salvar", key=f"btn_{ex_id}"):
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
                        st.cache_data.clear()
                        st.success("Salvo na planilha!")
                        st.rerun()
                    else:
                        st.error("Aba de histórico não encontrada.")

                with st.expander("Ver Postura / Dicas"):
                    st.write(row.get("Instrucoes_Postura", "Execute com técnica controlada."))

        if st.button("🏁 FINALIZAR TREINO DO DIA", type="primary"):
            st.balloons()
            st.success("Treino concluído e registrado com sucesso!")
    elif df_exercicios.empty and not msg_status:
        st.warning("Carregando base de dados...")

with tab_historico:
    st.subheader("Histórico Completo")
    if not df_historico.empty:
        st.dataframe(df_historico, use_container_width=True)
    else:
        st.info("Nenhuma série salva na aba de histórico ainda.")

with tab_nutricao:
    st.subheader("Metas Nutricionais (~3.000 kcal)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Proteína", "160g")
    m2.metric("Carboidrato", "400g")
    m3.metric("Gordura", "85g")
    st.markdown("""
    **Guia Prático da Mão:**
    * 🖐️ **Palma:** ~150g de frango ou carne bovina
    * ✊ **Punho:** ~100g de arroz ou batata
    * 👍 **Polegar:** ~15g de azeite ou pasta de amendoim
    """)
