import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key and api_key != "paste_your_api_key_here":
    genai.configure(api_key=api_key)
else:
    api_key = None

# Define the formal HSE prompt
HSE_PROMPT = """
Act as a formal and highly rigorous Health, Safety, and Environment (HSE) Inspector. Review the attached image carefully. 

Please provide a formal analysis formatted exactly like this:

**HAZARD IDENTIFICATION REPORT**
*   **Hazard:** [Name the specific hazard seen in the image]
*   **Risk Level:** [Low / Medium / High]
*   **Immediate Control Measure:** [What should be done right now to secure the area]
*   **Long-Term Preventative Action:** [How to prevent this from happening again in the future]

If you see multiple hazards, list them out sequentially using the format above. Keep your tone strictly professional and objective.
"""

# Streamlit App UI
st.set_page_config(page_title="AI Hazard Scanner", page_icon="⚠️", layout="centered")

# Custom CSS to force a mobile-like narrow layout on desktop
st.markdown("""
    <style>
    /* Force the main container to simulate a mobile screen */
    .block-container {
        max-width: 450px !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        margin: 0 auto !important;
        border: 2px solid #333;
        border-radius: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        background-color: rgba(20, 24, 33, 0.6); /* Slight background to separate from body */
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚠️ AI Safety Inspector")
st.markdown("Upload a photo of a worksite or potential hazard, and the AI will generate a formal HSE report.")

if not api_key:
    st.warning("⚠️ API Key not found! Please open the `.env` file in your folder and paste your Gemini API key.")

input_method = st.radio("Choose input method:", ["📁 Upload File", "📸 Use Camera"], horizontal=True)

final_file = None
if input_method == "📁 Upload File":
    final_file = st.file_uploader("Upload or take a photo...", type=["jpg", "jpeg", "png"])
else:
    final_file = st.camera_input("Take a photo using your device camera")

if final_file is not None:
    # Display the uploaded image
    image = Image.open(final_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Analyze Hazard", type="primary"):
        if not api_key:
            st.error("Cannot analyze: Missing API Key.")
        else:
            with st.spinner("Analyzing image for safety hazards..."):
                try:
                    # Initialize the model
                    model = genai.GenerativeModel('gemini-3.5-flash')
                    
                    # Generate the response
                    response = model.generate_content([HSE_PROMPT, image])
                    
                    # Display the result
                    st.success("Analysis Complete!")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
