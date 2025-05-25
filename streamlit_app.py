import streamlit as st
import time
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎉",
    layout="centered",
)

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #FF69B4;
            text-align: center;
        }
        .subtitle {
            font-size: 1.5em;
            text-align: center;
            color: #ff4b4b;
        }
        .message-box {
            background-color: #fff0f5;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 0 20px rgba(255,105,180,0.4);
        }
        .photo {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Balloon animation
#st.balloons()
# Continuous balloon-style animation on page load
balloon_loop_js = """
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
    const defaults = {
        spread: 70,
        startVelocity: 30,
        gravity: 0.3,
        ticks: 150,
        zIndex: 0,
    };

    function shootBalloon() {
        confetti(Object.assign({}, defaults, {
            particleCount: 5,
            origin: { x: Math.random(), y: 1.2 },
            colors: ['#FF69B4', '#FFD700', '#87CEFA', '#FF4500']
        }));
    }

    setInterval(shootBalloon, 300);  // Repeat every 300ms
</script>
"""

html(balloon_loop_js)

# Title and subtitle
st.markdown('<div class="title">🎉 Happy Birthday, Dear Anila Teacher! 🎂</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Wishing you a day filled with love, joy, and inspiration!</div>', unsafe_allow_html=True)
st.markdown("")
# Message box
with st.expander("Message Box (open with a sweet smile!)❤️"):
    with st.container():
        #st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.markdown('''
        <div class="message-box">
        <p>Dear Teacher,</p>
        <p>Today, we celebrate not only your birthday, but also the light and knowledge you've brought into our lives. 
        Your wisdom, patience, and kindness inspire us daily. Thank you for everything you do.</p>
        <p>May your year ahead be filled with endless opportunities and dreams come true! 🎁🎊</p>
        <p>With love, ❤️</p>
        <p>Your Grateful Student 🌟</p>
        </div>
        ''', unsafe_allow_html=True)

    
# Image placeholder (optional)
uploaded_file = st.file_uploader("Upload a memorable photo", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Happy moments!", use_column_width=True)

# Embed confetti animation using HTML + JavaScript
confetti_script = """
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
    const duration = 5 * 1000;
    const animationEnd = Date.now() + duration;
    const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

    function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    const interval = setInterval(function() {
        const timeLeft = animationEnd - Date.now();

        if (timeLeft <= 0) {
            return clearInterval(interval);
        }

        const particleCount = 50 * (timeLeft / duration);
        confetti(Object.assign({}, defaults, {
            particleCount,
            origin: { x: randomInRange(0.1, 0.9), y: Math.random() - 0.2 }
        }));
    }, 250);
</script>
"""
html(confetti_script)

# Optional: Background music
music_url = st.text_input("Enter background music URL (YouTube or MP3)", "")
if music_url:
    if "youtube.com" in music_url or "youtu.be" in music_url:
        st.video(music_url)
    else:
        st.audio(music_url)

# Footer
st.markdown("---")
st.markdown("🎈 Created with ❤️ using Streamlit")

