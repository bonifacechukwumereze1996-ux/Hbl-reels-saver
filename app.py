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
# STYLES (PRO SAAS DESIGN)
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f1117, #1b1f2a);
    color: white;
}

/* Glass card */
.card {
    background: rgba(255,255,255,0.06);
    padding: 22px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 18px;
}

/* Title */
.title {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #b0b3b8;
    margin-bottom: 15px;
}

/* Button */
.stButton>button {
    background-color: #1f6feb;
    color: white;
    border-radius: 10px;
    padding: 10px;
    width: 100%;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #2b7fff;
}

/* Feature boxes */
.feature {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="card">

<h1 class="title">⚡ HBL Reels Saver</h1>

<p class="subtitle">
Download Facebook & Instagram Reels in seconds
</p>

<img src="https://images.unsplash.com/photo-1611162616475-46b635cb6868"
style="width:100%; border-radius:14px; margin-top:10px;">

</div>
""", unsafe_allow_html=True)

# -----------------------------
# FEATURES
# -----------------------------
st.markdown("### Why Choose HBL Saver?")

f1, f2 = st.columns(2)
with f1:
    st.markdown('<div class="feature">⚡ Fast Downloads</div>', unsafe_allow_html=True)
with f2:
    st.markdown('<div class="feature">🎬 Reel Support</div>', unsafe_allow_html=True)

f3, f4 = st.columns(2)
with f3:
    st.markdown('<div class="feature">📱 Mobile Friendly</div>', unsafe_allow_html=True)
with f4:
    st.markdown('<div class="feature">🔒 Safe Processing</div>', unsafe_allow_html=True)

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
# DOWNLOAD BUTTON
# -----------------------------
if st.button("🚀 Download Now"):

    if not url:
        st.warning("Please paste a link first")

    elif "facebook.com" not in url and "instagram.com" not in url:
        st.error("❌ Only Facebook & Instagram links allowed")

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