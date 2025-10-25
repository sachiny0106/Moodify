from pathlib import Path
#Imports for streamlit
import streamlit as st
import av
import cv2
from streamlit_webrtc import (
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

#Imports for ml model
import numpy as np
# import mediapipe as mp # Moved to processor
# from keras.models import load_model # Moved to processor

from emotion_processor import EmotionProcessor


st.set_page_config(
    page_title="Moodify",
    page_icon="🎵",
)

page_bg_img = """
<style>

div.stButton > button:first-child {
    all: unset;
    width: 120px;
    height: 40px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #0f001a;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 50px;
}

div.stButton > button:hover::before {
    transform: translate(5%, 20%);
    width: 110%;
    height: 110%;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 5%);
}



[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1613327986042-63d4425a1a5d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background : black;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""
add_logo("https://github.com/NebulaTris/vibescape/blob/main/logo.png?raw=true")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Moodify 🎉🎶")
st.sidebar.success("Select a page below.")
st.sidebar.text("Developed by You")

st.markdown("**Hey there, emotion explorer! Are you ready for a wild ride through the rollercoaster of feelings?** 🎢🎵")
st.markdown("**Welcome to Moodify, where our snazzy AI meets your wacky emotional world head-on! We've got our virtual goggles on (nope, not really, but it sounds cool** 😎 **) to analyze your emotions using a webcam. And what do we do with all those emotions, you ask? We turn them into the most toe-tapping, heartwarming, and occasionally hilarious music playlists you've ever heard!** 🕺💃")
st.markdown("**You've heard of Spotify, SoundCloud, and YouTube, right? Well, hold onto your hats because Moodify combines these musical behemoths into one epic entertainment extravaganza! Now you can dive into your favorite streaming services with a twist — they'll be serving up songs based on your mood!** 🎶")
st.markdown("**Feeling like a happy-go-lucky panda today? We've got a playlist for that! Or perhaps you've got the moody blues? No worries, Moodify has your back. Our AI wizardry detects your vibes and serves up the tunes that match your moment.** 🐼🎉")
st.markdown("**So, get ready for a whirlwind of emotions and music. Moodify is here to turn your webcam into a mood ring, your screen into a dance floor, and your heart into a DJ booth. What's next? Well, that's entirely up to you and your ever-changing feelings!**")
st.markdown("**So, strap in** 🚀 **, hit that webcam** 📷 **, and let the musical journey begin! Moodify is your ticket to a rollercoaster of emotions, all set to your favorite tunes.** 🎢🎵")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{
        "urls": ["stun:stun.l.google.com:19302"]
    }]})

# CWD path
HERE = Path(__file__).parent


# Validating emotion file existence
try:
    if not Path("emotion.npy").exists():
        np.save("emotion.npy", np.array([""]))
except Exception:
    pass

if "run" not in st.session_state:
    st.session_state["run"] = ""

try:
    emotion = np.load("emotion.npy")[0]
except:
    emotion = ""

if not emotion:
    st.session_state["emotion"] = ""
else:
    st.session_state["emotion"] = emotion



    


webrtc_streamer(key="key", desired_playing_state=st.session_state.get("run", "") == "true" ,mode=WebRtcMode.SENDRECV,  rtc_configuration=RTC_CONFIGURATION, video_processor_factory=EmotionProcessor, media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True)


col1, col2, col6 = st.columns([1, 1, 1])

with col1:
    start_btn = st.button("Start")
with col6:
    stop_btn = st.button("Stop")

if start_btn:
    st.session_state["run"] = "true"
    st.experimental_rerun()

if stop_btn:
    st.session_state["run"] = "false"
    st.experimental_rerun()
else:
    if not emotion:
        pass
    else:
        np.save("emotion.npy", np.array([""]))
        st.session_state["emotion"] = run
        st.success("Your current emotion is: " + emotion)
        st.subheader("Choose your streaming service")

col3, col4, col5 = st.columns(3)

with col4:
    btn = st.button("Spotify")
    if btn:
        switch_page("Spotify")

with col5:
    btn2 = st.button("Youtube")
    if btn2:
        switch_page("Youtube")

with col3:
    btn3 = st.button("Soundcloud")
    if btn3:
        switch_page("Soundcloud")
