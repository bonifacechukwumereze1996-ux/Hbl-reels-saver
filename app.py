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
    <h2>⚡Disclaimer </h2>
    <h3>Welcome to HBL Reels Saver.</h3>
    <p>
      This platform is designed to help fashion designers, clothing brands, tailors, students, and clients conveniently save publicly available fashion reels and clothing design inspiration from supported social media platforms for personal reference, learning, and creative inspiration.  <br>
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

    url = st.text_input("***📎PASTE REELS HERE***")

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
##About Us
Welcome to HBL Reels Saver, a digital solution developed by HBL Skill Global.
HBL Skill Global is committed to empowering individuals and businesses through fashion, digital innovation, and practical technology solutions. We believe that creativity grows when people have access to quality learning resources and design inspiration.
HBL Reels Saver was created to help fashion designers, tailors, clothing brands, students, and fashion enthusiasts easily save publicly available reels from supported social media platforms for inspiration, learning, and personal reference.
Our mission is to bridge the gap between fashion and technology by providing simple, reliable, and user-friendly tools that support creativity and productivity.

Thank you for choosing HBL Reels Saver.
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
st.caption("© 2026 HBL Skill Global. All Rights Reserved.
")
