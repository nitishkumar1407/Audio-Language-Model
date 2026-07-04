import streamlit as st
import requests
import tempfile
from audiorecorder import audiorecorder

# =========================================
# CONFIG
# =========================================
API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="AHNA AI Studio",
    page_icon="🎧",
    layout="wide"
)

# =========================================
# MODERN UI CSS
# =========================================
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* Title */
.title {
    font-size: 52px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Card */
.card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    border-radius: 12px;
    padding: 14px;
    font-size: 16px;
    font-weight: 700;
    border: none;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* Metrics */
.metric-box {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Result Box */
.result {
    background: rgba(0,0,0,0.4);
    padding: 18px;
    border-radius: 15px;
    border-left: 4px solid #60a5fa;
    margin-top: 10px;
    white-space: pre-wrap;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    padding: 10px 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================
st.markdown('<div class="title">🎧 AHNA AI STUDIO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Next-Gen Audio Intelligence System</div>', unsafe_allow_html=True)

# =========================================
# TABS
# =========================================
tab1, tab2 = st.tabs(["📁 Upload Audio", "🎙️ Live Recording"])

# =========================================
# TAB 1 - UPLOAD
# =========================================
with tab1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    file = st.file_uploader("📂 Drag & Drop or Browse Audio", type=["wav", "mp3", "m4a"])

    if file:

        st.audio(file)

        if st.button("🚀 Analyze Audio", key="upload_btn"):

            with st.spinner("🧠 AI is analyzing your audio..."):

                files = {
                    "file": (
                        file.name,
                        file.getvalue(),
                        file.type
                    )
                }

                res = requests.post(API_URL, files=files)

                if res.status_code == 200:
                    data = res.json()

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
                        st.metric("🧠 Status", "Processed")
                        st.markdown('</div>', unsafe_allow_html=True)

                        st.markdown('<div class="result">', unsafe_allow_html=True)
                        st.subheader("📝 Transcript")
                        st.write(data.get("transcription", "Not found"))
                        st.markdown('</div>', unsafe_allow_html=True)

                    with col2:
                        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
                        st.metric("⚡ AI Engine", "LLaMA + Whisper")
                        st.markdown('</div>', unsafe_allow_html=True)

                        st.markdown('<div class="result">', unsafe_allow_html=True)
                        st.subheader("🧠 Reasoning")
                        st.write(data.get("reasoning", "Not found"))
                        st.markdown('</div>', unsafe_allow_html=True)

                else:
                    st.error(res.text)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# TAB 2 - LIVE RECORDING
# =========================================
with tab2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    audio = audiorecorder("🎤 Start Recording", "⏹️ Stop Recording")

    if audio:

        st.audio(audio.export().read())

        if st.button("🧠 Analyze Recording", key="live_btn"):

            with st.spinner("Processing audio..."):

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    audio.export(tmp.name, format="wav")

                    files = {"file": open(tmp.name, "rb")}
                    res = requests.post(API_URL, files=files)

                if res.status_code == 200:
                    data = res.json()

                    st.success("Analysis Complete 🎉")

                    st.markdown('<div class="result">', unsafe_allow_html=True)
                    st.subheader("📝 Transcript")
                    st.write(data.get("transcription", "Not found"))

                    st.subheader("🧠 Reasoning")
                    st.write(data.get("reasoning", "Not found"))
                    st.markdown('</div>', unsafe_allow_html=True)

                else:
                    st.error(res.text)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# FOOTER
# =========================================
st.markdown("---")
st.markdown(
    "<center style='color:#94a3b8'>⚡ Built with Whisper • FastAPI • LLaMA • Streamlit</center>",
    unsafe_allow_html=True
)