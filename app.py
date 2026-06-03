import streamlit as st
import yt_dlp
import os
import time

DOWNLOAD_FOLDER = "downloads"

# Delete files older than 3 hours
if os.path.exists(DOWNLOAD_FOLDER):
    now = time.time()

    for filename in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)

        if os.path.isfile(file_path):
            if now - os.path.getmtime(file_path) > 10800:  # 3 hours
                os.remove(file_path)

# -----------------------------
# MUST BE FIRST STREAMLIT COMMAND
# -----------------------------
st.set_page_config(page_title="HBL Reels Saver (Fast Mode)", layout="centered")
st.markdown("""
<marquee>
🎬 Welcome to HBL Reels Saver | Fast Downloads | Secure Processing | No Login Required 🚀
</marquee>
<div style="
    background: linear-gradient(135deg, #0f1117, #1f2937);
    color: white;
    padding: 40px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
">
    <h1>⚡ HBL Reels Saver</h1>
    <h3>Download Facebook & Instagram Reels in Seconds</h3>
    <p>
        Fast • Secure • Free <br>
        Save your favorite reels with ease.
    </p>
</div>
""", unsafe_allow_html=True)
# -----------------------------
# STYLES
# -----------------------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: url(" https://images.unsplash.com/photo-1611162616475-46b635cb6868") no-repeat center center fixed;
    background-size: cover;
    color: white;
}

/* Navbar */
.navbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:8px;
    margin-bottom:15px;
    background:#161b22;
    border-radius:10px;
}

.logo-text {
    font-size:15px;
    font-weight:bold;
    color:white;
}
/* Text input box */
.stTextInput input {
    background-color: white !important;
    color: black !important;
}

/* Placeholder text */
.stTextInput input::placeholder {
    color: black !important;
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.image("logo.png", width=60)

st.markdown("""
<div class="navbar">
    <div class="logo-text">🎬 HBL Reels Saver</div> 
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
# FAST DOWNLOAD FUNCTION
# -----------------------------
def fast_download(video_url):

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        "format": "worst/best",
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
# PAGE 1 - INPUT
# -----------------------------
if st.session_state.step == 1:

    st.title("🎬 HBL Reels Saver (ABOUT US)")
    st.write("HBL Reels Saver is a simple and user-friendly tool designed to help users download Facebook and Instagram Reels quickly and easily.")
    url = st.text_input("***📎 PASTE REELS HERE***")

    if st.button("**CONTINUE ➡️**"):

        if not url:
            st.warning("Please paste a link")

        elif "facebook.com" not in url and "instagram.com" not in url:
            st.error("❌ Only Facebook & Instagram supported")

        else:
            st.session_state.url = url
            st.session_state.step = 2
            st.rerun()

# -----------------------------
# PAGE 2 - DOWNLOAD
# -----------------------------
if st.session_state.step == 2:

    st.title("⚡ Fast Download Mode")
    st.info("Processing link... please wait")

    if st.button("🚀 Start Fast Download"):

        try:
            start = time.time()

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
# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
## Disclaimer
HBL Reels Saver does not permanently store downloaded videos on its servers. Content is processed temporarily to facilitate downloads and is automatically removed afterward.
Users are responsible for ensuring they have the right to download and use any content accessed through this service and must comply with applicable laws and platform terms.
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
st.markdown("### Support HBL Reels Saver ❤️")
st.markdown("[Donate via Paystack](https://paystack.com/pay/yourlink)")