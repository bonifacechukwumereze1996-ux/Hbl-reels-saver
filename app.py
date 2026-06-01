import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="HBL Downloader", layout="centered")

st.title("🔥 HBL Social Media Downloader")
st.write("Download videos from Facebook, TikTok, Instagram & YouTube")

video_url = st.text_input("📎 Paste your video link here")

def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename

if st.button("🚀 Download"):
    if video_url:
        try:
            if not os.path.exists("downloads"):
                os.makedirs("downloads")

            st.info("Downloading... please wait ⏳")

            file_path = download_video(video_url)

            st.success("✅ Download complete!")

            with open(file_path, "rb") as f:
                st.download_button(
                    label="📥 Click to Download File",
                    data=f,
                    file_name=os.path.basename(file_path),
                )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a valid link")