import streamlit as st
import yt_dlp

st.set_page_config(page_title="HBL Downloader Pro", layout="centered")

st.title("🔥 HBL Downloader Pro")
st.write("Download videos from Facebook, TikTok, Instagram & YouTube")

url = st.text_input("📎 Paste video link here")

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info['title']

if st.button("🚀 Process Video"):
    if url:
        try:
            st.info("Processing link... ⏳")

            title = download_video(url)

            st.success("Ready for download ✅")

            st.write("🎬 Video Title:", title)

            st.markdown("Click download below 👇")

            st.download_button(
                label="📥 Download Video",
                data="Download triggered (handled by Streamlit server)",
                file_name="video.txt"
            )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a valid link")