import streamlit as st
import yt_dlp
import os
import time

st.set_page_config(page_title="HBL Reels Saver (Fast Mode)", layout="centered")

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