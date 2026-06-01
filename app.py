import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="HBL Reels Saver", layout="centered")

st.title("🔥 HBL Reels Saver")
st.write("Download Facebook & Instagram Reels easily")

url = st.text_input("📎 Paste Facebook or Instagram Reel link here")

# ✅ Restrict to only supported platforms
if url:
    if "facebook.com" not in url and "instagram.com" not in url:
        st.error("❌ Only Facebook and Instagram Reels are supported")
        st.stop()

DOWNLOAD_FOLDER = "downloads"

def download_reel(video_url):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        "format": "best",
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_path = ydl.prepare_filename(info)
        return file_path

if st.button("🚀 Download Reel"):
    if url:
        try:
            st.info("Processing reel... ⏳")

            file_path = download_reel(url)

            st.success("Download complete ✅")

            with open(file_path, "rb") as f:
                st.download_button(
                    label="📥 Save to Phone",
                    data=f,
                    file_name=os.path.basename(file_path),
                )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a valid link")