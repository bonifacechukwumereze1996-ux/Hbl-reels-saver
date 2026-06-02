import streamlit as st
import yt_dlp
import os
import time
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0f1117;
    color: white;
}

/* Hero card */
.hero {
    background: #161b22;
    padding: 30px;
    border-radius: 20px;
    text-align: right;
    margin-bottom: 25px;
    border: 1px solid #30363d;
}

/* Title */
.hero-title {
    font-size: 40px;
    font-weight: bold;
    color: Gold;
}

/* Subtitle */
.hero-subtitle {
    font-size: 16px;
    color: #b0b3b8;
}

/* Feature cards */
.feature-card {
    background: #161b22;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #30363d;
}

/* Navbar */
.navbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:15px;
    margin-bottom:20px;
    background:#161b22;
    border-radius:15px;
}

.logo-text {
    font-size:20px;
    font-weight:bold;
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="HBL Reels Saver (Fast Mode)", layout="centered")
st.image("logo.png", width=100)
st.markdown("""
<div class="navbar">
    <div class="logo-text">🔥 HBL Reels Saver</div>
    <div>Home | Features | About | Contact</div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <div class="hero-title">
        Save Facebook & Instagram Reels
    </div>

    <div class="hero-subtitle">
        Fast, secure and mobile-friendly downloads.
    </div>
</div>
""", unsafe_allow_html=True)

DOWNLOAD_FOLDER = "downloads"

# -----------------------------
# SESSION STATE
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "url" not in st.session_state:
    st.session_state.url = ""

# -----------------------------
# PAGE 1 - INPUT
# -----------------------------
if st.session_state.step == 1:

    st.title("⚡ HBL Reels Saver (FAST MODE)")
    st.write("Facebook & Instagram Reels Downloader")

    url = st.text_input("📎 Paste Reel link")

    if st.button("Continue ➡️"):
        if url:
            if "facebook.com" not in url and "instagram.com" not in url:
                st.error("❌ Only Facebook & Instagram supported")
            else:
                st.session_state.url = url
                st.session_state.step = 2
                st.rerun()
        else:
            st.warning("Please paste a link")

# -----------------------------
# FAST DOWNLOAD FUNCTION
# -----------------------------
def fast_download(video_url):

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        "format": "worst/best",   # ⚡ FAST MODE (no HD delay)
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "concurrent_fragment_downloads": 1
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_path = ydl.prepare_filename(info)
        return file_path

# -----------------------------
# PAGE 2 - DOWNLOAD
# -----------------------------
if st.session_state.step == 2:

    st.title("⚡ Fast Download Mode")

    st.info("Processing link... please wait")

    # platform check
    if "facebook.com" not in st.session_state.url and "instagram.com" not in st.session_state.url:
        st.error("Invalid link")
        st.stop()

    if st.button("🚀 Start Fast Download"):

        try:
            start = time.time()

            st.write("⬇️ Downloading...")

            file_path = fast_download(st.session_state.url)

            duration = round(time.time() - start, 2)

            st.success(f"Done in {duration} seconds ✅")

            with open(file_path, "rb") as f:
                st.download_button(
                    label="📥 Save to Phone",
                    data=f,
                    file_name=os.path.basename(file_path),
                )

        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("⬅️ Back"):
        st.session_state.step = 1
st.markdown("""
## Download Facebook & Instagram Reels

Fast, simple and mobile-friendly reel downloader.

Paste your reel link below and save it to your device in seconds.
""")
st.markdown("## Why Choose HBL Reels Saver?")

col1, col2 = st.columns(2)

with col1:
    st.success("⚡ Fast Downloads")

with col2:
    st.success("🎬 Reel Support")

col3, col4 = st.columns(2)

with col3:
    st.success("📱 Mobile Friendly")

with col4:
    st.success("🔒 Secure Processing")

st.markdown("---")
st.caption("© 2026 HBL Reels Saver | All Rights Reserved")