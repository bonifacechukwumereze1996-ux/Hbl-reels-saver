import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="HBL Reels Saver", layout="centered")

DOWNLOAD_FOLDER = "downloads"

# -----------------------------
# SESSION STATE CONTROL
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "url" not in st.session_state:
    st.session_state.url = ""

if "info" not in st.session_state:
    st.session_state.info = None

# -----------------------------
# PAGE 1 - LINK INPUT
# -----------------------------
if st.session_state.step == 1:

    st.title("🔥 HBL Reels Saver")
    st.write("Paste Facebook or Instagram Reel link")

    url = st.text_input("📎 Enter Reel Link")

    if st.button("Next ➡️"):
        if url:
            if "facebook.com" not in url and "instagram.com" not in url:
                st.error("❌ Only Facebook & Instagram supported")
            else:
                st.session_state.url = url
                st.session_state.step = 2
                st.rerun()
        else:
            st.warning("Please enter a link")

# -----------------------------
# FUNCTION TO GET VIDEO INFO
# -----------------------------
def get_video_info(video_url):
    ydl_opts = {"quiet": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info

# -----------------------------
# DOWNLOAD FUNCTION
# -----------------------------
def download_video(video_url, quality):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    if quality == "low":
        fmt = "worst"
    elif quality == "hd":
        fmt = "best[height<=720]"
    else:
        fmt = "best"

    ydl_opts = {
        "format": fmt,
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_path = ydl.prepare_filename(info)
        return file_path

# -----------------------------
# PAGE 2 - QUALITY SELECTION
# -----------------------------
if st.session_state.step == 2:

    st.title("🎬 Choose Quality")

    st.write("Your link is ready for download")

    try:
        if st.session_state.info is None:
            st.session_state.info = get_video_info(st.session_state.url)

        st.success("Video Loaded ✅")

        st.write("📌 Title:", st.session_state.info.get("title", "Unknown"))

    except:
        st.error("Failed to load video info")
        st.stop()

    quality = st.radio(
        "Select Quality",
        ["High Quality", "HD (Recommended)", "Low Quality"]
    )

    if st.button("🚀 Download Now"):

        if quality == "Low Quality":
            q = "low"
        elif quality == "HD (Recommended)":
            q = "hd"
        else:
            q = "best"

        st.info("Downloading... ⏳")

        try:
            file_path = download_video(st.session_state.url, q)

            st.success("Download complete ✅")

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
        st.session_state.info = None
        st.rerun()