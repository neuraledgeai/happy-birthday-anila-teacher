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
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

        @keyframes glow {
            0% {
                box-shadow: 0 0 10px rgba(255,105,180,0.3);
                border-image: linear-gradient(45deg, #FF69B4, #FFD700) 1;
            }
            50% {
                box-shadow: 0 0 25px rgba(255,105,180,0.6);
                border-image: linear-gradient(45deg, #FFD700, #FF69B4) 1;
            }
            100% {
                box-shadow: 0 0 10px rgba(255,105,180,0.3);
                border-image: linear-gradient(45deg, #FF69B4, #FFD700) 1;
            }
        }

        @keyframes bounceIn {
            0% {
                transform: scale(0.9);
                opacity: 0;
            }
            60% {
                transform: scale(1.05);
                opacity: 1;
            }
            100% {
                transform: scale(1);
            }
        }

        .title {
            font-size: 3em;
            font-weight: bold;
            color: #FF69B4;
            text-align: center;
            font-family: 'Quicksand', sans-serif;
        }

        .subtitle {
            font-size: 1.5em;
            text-align: center;
            color: #ff4b4b;
            font-family: 'Quicksand', sans-serif;
        }

        .message-box {
            font-family: 'Quicksand', sans-serif;
            background: linear-gradient(135deg, #fff0f5, #ffe6fa);
            border-radius: 20px;
            padding: 35px;
            margin-top: 30px;
            animation: glow 4s ease-in-out infinite, bounceIn 1.5s ease;
            border: 3px solid transparent;
            border-image-slice: 1;
        }

        .message-box p {
            font-size: 1.2em;
            color: #cc3366;
            line-height: 1.6;
            margin-bottom: 10px;
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

st.markdown("")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown(" js sjks sjs sjs  ")
with col2:
    if st.button("🎁 Open Your Birthday Surprise!"):
        st.success("💖 Surprise! You’ve just unwrapped a treasure chest of gratitude and love! 🎁")
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




