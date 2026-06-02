import streamlit as st
import yt_dlp
import os
import time

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(page_title="HBL Reels Saver", layout="centered")

DOWNLOAD_FOLDER = "downloads"

# -----------------------------
# STYLES
# -----------------------------
st.markdown("""
<style>

/* Background image */
.stApp {
    background: url("https://images.unsplash.com/photo-1611162617474-5b21e879e113") no-repeat center center fixed;
    background-size: cover;
    color: white;
}

/* Dark overlay */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.78);
    z-index: -1;
}

/* Navbar */
.navbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:10px 15px;
    margin-bottom:20px;
    background: rgba(22, 27, 34, 0.85);
    border-radius:12px;
    backdrop-filter: blur(10px);
}

/* Logo */
.logo {
    display:flex;
    align-items:center;
}

.logo img {
    width:32px;
    height:32px;
    border-radius:6px;
}

.logo span {
    font-size:15px;
    font-weight:bold;
    margin-left:8px;
    color:white;
}

/* Nav links */
.nav-links a {
    font-size:12px;
    color:#b0b3b8;
    text-decoration:none;
    margin-left:10px;
}

.nav-links a:hover {
    color:white;
    transition:0.3s;
}

/* Watermark */
.watermark {
    position: fixed;
    opacity: 0.05;
    width: 90px;
    z-index: -1;
}

.fb {
    top: 18%;
    left: 8%;
}

.ig {
    bottom: 12%;
    right: 8%;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# WATERMARK LOGOS
# -----------------------------
st.markdown("""
<img class="watermark fb" src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg">
<img class="watermark ig" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png">
""", unsafe_allow_html=True)

# -----------------------------
# NAVBAR (FIXED)
# -----------------------------
st.markdown("""
<div class="navbar">
    <div class="logo">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg">
        <span>HBL Saver</span>
    </div>

    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.title("⚡ HBL Reels Saver")
st.write("Download Facebook & Instagram Reels in seconds")

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
# INPUT
# -----------------------------
url = st.text_input("📎 Paste Reel Link")

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
if st.button("🚀 Download Now"):

    if not url:
        st.warning("Please paste a link")

    elif "facebook.com" not in url and "instagram.com" not in url:
        st.error("❌ Only Facebook & Instagram links allowed")

    else:
        try:
            start = time.time()

            st.info("Downloading... please wait ⏳")

            file_path = fast_download(url)

            duration = round(time.time() - start, 2)

            st.success(f"Done in {duration} seconds ✅")

            with open(file_path, "rb") as f:
                st.download_button(
                    "📥 Save to Phone",
                    f,
                    file_name=os.path.basename(file_path)
                )

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# FEATURES
# -----------------------------
st.markdown("---")
st.markdown("## Why Choose HBL Saver?")

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

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("© 2026 HBL Reels Saver | All Rights Reserved")