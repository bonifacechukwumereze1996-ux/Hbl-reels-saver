import streamlit as st
import yt_dlp
import os
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="HBL Reels Saver",
    page_icon="⚡",
    layout="centered"
)

DOWNLOAD_FOLDER = "downloads"

# -----------------------------
# CLEAN THEME (NO HTML CSS)
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f1117;
    }

    h1, h2, h3, p, label {
        color: white !important;
    }

    .stButton>button {
        background-color: #1f6feb;
        color: white;
        border-radius: 8px;
        padding: 10px 16px;
        border: none;
        width: 100%;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #2b7fff;
    }

    .block-container {
        padding-top: 2rem;
    }

    </style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER (STREAMLIT SAFE)
# -----------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("## ⚡")

with col2:
    st.title("HBL Reels Saver")
    st.caption("Download Facebook & Instagram Reels easily")

st.markdown("---")

# -----------------------------
# FEATURES (SAFE UI)
# -----------------------------
st.subheader("Why Choose HBL Saver?")

f1, f2 = st.columns(2)
f1.success("⚡ Fast Downloads")
f2.success("🎬 Reel Support")

f3, f4 = st.columns(2)
f3.success("📱 Mobile Friendly")
f4.success("🔒 Safe Processing")

st.markdown("---")

# -----------------------------
# DOWNLOAD FUNCTION
# -----------------------------
def fast_download(video_url):

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        "format": "best",
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        return ydl.prepare_filename(info)

# -----------------------------
# INPUT SECTION
# -----------------------------
url = st.text_input("📎 Paste Facebook or Instagram Reel Link")

# -----------------------------
# DOWNLOAD ACTION
# -----------------------------
if st.button("🚀 Download Now"):

    if not url:
        st.warning("Please paste a link first")

    elif "facebook.com" not in url and "instagram.com" not in url:
        st.error("Only Facebook & Instagram links allowed")

    else:
        try:
            start = time.time()

            with st.spinner("Downloading video... please wait ⏳"):
                file_path = fast_download(url)

            duration = round(time.time() - start, 2)

            st.success(f"Download completed in {duration} seconds ✅")

            with open(file_path, "rb") as f:
                st.download_button(
                    "📥 Save to Device",
                    f,
                    file_name=os.path.basename(file_path)
                )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("© 2026 HBL Reels Saver | Built for fast mobile downloads")