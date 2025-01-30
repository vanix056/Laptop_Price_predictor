import streamlit as st
import pickle
import numpy as np
from streamlit.components.v1 import html

# Custom CSS with enhanced animations and new background
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #2A2356 0%, #0B0B2C 100%);
    color: #ffffff;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes ripple {
    to { transform: scale(4); opacity: 0; }
}

.card {
    animation: slideIn 0.8s ease-out;
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 25px;
    margin: 15px 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
    transform: translateY(-5px) rotate(2deg);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
}

.stSelectbox, .stNumberInput {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
}

.stSelectbox:focus-within, .stNumberInput:focus-within {
    border-color: #7C4DFF !important;
    box-shadow: 0 0 15px rgba(124, 77, 255, 0.3) !important;
}

.stButton>button {
    border-radius: 30px !important;
    background: linear-gradient(135deg, #7C4DFF 0%, #FF6B6B 100%) !important;
    color: white !important;
    border: none !important;
    padding: 16px 32px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease !important;
}

.stButton>button:hover {
    animation: pulse 1.5s infinite;
    box-shadow: 0 10px 25px rgba(124, 77, 255, 0.4) !important;
}

.stButton>button:active:after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    background: rgba(255, 255, 255, 0.4);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    animation: ripple 0.6s ease-out;
}

.price-result {
    background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%) !important;
    padding: 30px;
    border-radius: 20px;
    margin-top: 30px;
    animation: slideIn 0.6s ease-out;
    position: relative;
    overflow: hidden;
}

.price-result:before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
    transform: rotate(45deg);
    animation: shine 3s infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(100%) rotate(45deg); }
}

h1 {
    animation: float 3s ease-in-out infinite;
    text-align: center;
    background: linear-gradient(45deg, #7C4DFF, #FF6B6B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 30px !important;
}

</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_models():
    pipe = pickle.load(open('pipe.pickle','rb'))
    data_frame = pickle.load(open('read_csv.pickle','rb'))
    return pipe, data_frame

pipe, data_frame = load_models()

# Page layout
st.title('🚀 FutureTech Laptop Configurator')
st.markdown("##### ✨ Design your perfect machine and see instant pricing magic!")

# Split form into columns
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("### 🌟 Basic Specs")
        brand = st.selectbox("**Brand**", data_frame['Company'].unique(), key='brand')
        type_name = st.selectbox("**Type**", data_frame['TypeName'].unique(), key='type')
        ram = st.selectbox("**RAM (GB)**", data_frame['Ram'].unique(), key='ram')

with col2:
    with st.container():
        st.markdown("### 💾 Storage")
        hdd = st.selectbox("**HDD Storage**", [0,128,256,512,1024,2048], key='hdd')
        ssd = st.selectbox("**SSD Storage**", [0,8,128,256,512,1024], key='ssd')

# Advanced Configuration
with st.expander("🔧 Advanced Settings", expanded=False):
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### 🧠 Processing")
        cpu = st.selectbox("**Processor**", data_frame['Cpu brand'].unique(), key='cpu')
        gpu = st.selectbox("**Graphics**", data_frame['Gpu brand'].unique(), key='gpu')
        
    with col4:
        st.markdown("### 🖥️ Display")
        os = st.selectbox("**OS**", data_frame['os'].unique(), key='os')
        touch = st.selectbox("**Touchscreen**", ['No','Yes'], key='touch')
        display = st.selectbox("**IPS Display**", ['No','Yes'], key='display')

# Physical Specs
with st.container():
    st.markdown("### ⚖️ Physical Attributes")
    pcol1, pcol2 = st.columns(2)
    
    with pcol1:
        weight = st.number_input('**Weight (kg)**', min_value=0.5, max_value=5.0, step=0.1, key='weight')
    
    with pcol2:
        screen_size = st.number_input("**Screen Size**", min_value=10.0, max_value=17.0, step=0.1, key='screen')
        resolution = st.selectbox('**Resolution**', ['1920x1080','1366x768','1600x900','3840x2160',
                                                    '3200x1800','2880x1800','2560x1600','2560x1440',
                                                    '2304x1440'], key='resolution')

# Prediction Button
if st.button('✨ PREDICT PRICE ✨', use_container_width=True):
    with st.spinner('🚀 Launching prediction sequence...'):
        # Input processing
        touch = 1 if touch == 'Yes' else 0
        display = 1 if display == 'Yes' else 0
        
        xres = int(resolution.split('x')[0])
        yres = int(resolution.split('x')[1])
        ppi = ((xres**2) + (yres**2))**0.5 / screen_size if screen_size > 0 else 0
        
        q = np.array([brand, type_name, ram, weight, touch, display, ppi, cpu, hdd, ssd, gpu, os])
        q = q.reshape(1, 12)
        
        price_pkr = int(np.exp(pipe.predict(q)[0]))
        price_inr = int(price_pkr / 3.22)
        
        # Animated result display
        st.markdown(f"""
        <div class="price-result">
            <div style="text-align: center; position: relative; z-index: 2;">
                <h2 style="margin:0 0 20px 0;">💎 Estimated Price Revelation 💎</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 15px;">
                        <div style="font-size: 1.5em;">🇵🇰 PKR</div>
                        <div style="font-size: 2.5em; font-weight: 800;">{price_pkr:,}</div>
                    </div>
                    <div style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 15px;">
                        <div style="font-size: 1.5em;">🇮🇳 INR</div>
                        <div style="font-size: 2.5em; font-weight: 800;">{price_inr:,}</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Floating Particles Effect (Optional)
html('''
<div id="particles"></div>
<script>
// Add floating particles animation
document.write('<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"><\/script>');
setTimeout(() => {
    particlesJS('particles', {
        particles: {
            number: { value: 50 },
            color: { value: '#7C4DFF' },
            shape: { type: 'circle' },
            opacity: { value: 0.5 },
            size: { value: 3 },
            move: {
                enable: true,
                speed: 1,
                direction: 'none',
                random: true,
                straight: false,
                out_mode: 'out',
                bounce: false,
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: { enable: true, mode: 'repulse' },
                onclick: { enable: true, mode: 'push' },
                resize: true
            }
        },
        retina_detect: true
    });
}, 500);
</script>
<style>
#particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}
</style>
''')

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #888;">
    🔮 Powered by Streamlit | 🌐 Made by Vanix056
</div>
""", unsafe_allow_html=True)
