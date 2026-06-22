# ⚠️ AI Safety Inspector

A professional, mobile-friendly Health, Safety, and Environment (HSE) application built with Python and Streamlit. This application leverages the cutting-edge **Google Gemini 3.5 Vision API** to act as an automated, highly rigorous safety inspector.

## Features
* **Mobile-Friendly UI**: Designed with a responsive, app-like interface for use on the field.
* **Camera Integration**: Allows field workers to snap photos of potential hazards directly from their mobile browser.
* **Automated Formal Reporting**: Instantly generates structured HSE reports detailing the hazard, risk level, immediate control measures, and long-term preventative actions.
* **High Efficiency**: Processes complex visual environments in seconds using Cloud AI, requiring zero local hardware acceleration.

## Setup & Installation

1. **Clone or Download** this repository.
2. **Install Dependencies**: Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
3. **API Key Setup**: Create a `.env` file in the root directory and add your Google Gemini API Key:
   ```env
   GEMINI_API_KEY="Your_API_Key_Here"
   ```

## Running the Application

To launch the application locally, run the following command in your terminal:
```bash
python -m streamlit run app.py
```
The app will automatically open in your default web browser.

## Deployment
This application is fully optimized for **Streamlit Community Cloud**. 
Simply upload these files to a GitHub repository, connect it to Streamlit Cloud, and add your `GEMINI_API_KEY` to the Advanced Secrets settings to host the application for free.
