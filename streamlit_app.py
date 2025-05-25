import streamlit as st
import time
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎉",
    layout="centered",
)

st.markdown("""
<style>
/* Title & subtitle styles */
.title {
    font-size: 3em;
    font-weight: bold;
    color: #FF69B4;
    text-align: center;
    margin-bottom: 0.2em;
}
.subtitle {
    font-size: 1.5em;
    text-align: center;
    color: #ff4b4b;
    margin-bottom: 2em;
}

/* Message box styles */
.message-box {
    background-color: #fff0f5;
    border-radius: 15px;
    padding: 30px;
    margin-top: 30px;
    box-shadow: 0 0 20px rgba(255,105,180,0.4);
    font-size: 1.1em;
    line-height: 1.6em;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s;
}
.message-box:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(255,105,180,0.6);
}

/* Center image */
.photo {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

/* Expander animation */
[data-testid="stExpander"] > summary {
    font-weight: bold;
    font-size: 1.3em;
    color: #FF69B4;
    animation: pulseGlow 2s ease-in-out infinite;
    text-align: center;
    cursor: pointer;
}
@keyframes pulseGlow {
    0% {
        text-shadow: 0 0 5px #ff4b91, 0 0 10px #ff4b91;
    }
    50% {
        text-shadow: 0 0 15px #ff99c8, 0 0 25px #ff99c8;
    }
    100% {
        text-shadow: 0 0 5px #ff4b91, 0 0 10px #ff4b91;
    }
}

/* Signature (handwritten) */
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
.signature {
    font-family: 'Pacifico', cursive;
    color: #FF69B4;
    font-size: 1.8em;
    text-align: center;
    margin-top: 20px;
}

/* Optional: Hide Streamlit footer */
footer {visibility: hidden;}
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
with st.expander("💝 “A Heartfelt Note Just for You – Open With a Smile 😊"):
    st.markdown('<div style="text-align:center; font-size:2em;">💌</div>', unsafe_allow_html=True)
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
        st.balloons()
        st.markdown("")
        st.audio(data="birthday_song.mpeg", loop = True, autoplay = True)

if st.button("🎈 Open Your Birthday Surprise Here!"):
    st.success("✨🎉 Ta-da! ✨ A bundle of gratitude and admiration, wrapped in love — just for you 💝")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjllcWE3YnZncTlsOXdkcHIzM3d0cDJqamswNHEyYWhyOWdscXMweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iB6I46FbLRqsLliGpI/giphy.gif", width=300)


# Footer
st.markdown("---")

# Something amazing to be done here
st.markdown("""
    > *"To teach is to touch a life forever"*  
    > — Jerry Whittle
""")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .signature {
        font-family: 'Pacifico', cursive;
        color: #FF69B4;
        font-size: 1.8em;
        text-align: center;
        margin-top: 20px;
    }
    </style>

    <div class="signature">💖 Forever grateful, with all my heart 💕</div>
""", unsafe_allow_html=True)




