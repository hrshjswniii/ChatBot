import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("google_api")

if not GOOGLE_API_KEY:
    st.error("Missing Google API key in .env (variable: google_api)")
    st.stop()

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("💬 Gemini Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your message:", key="user_input")

if st.button("Send") and user_input.strip():
    with st.spinner("Generating response..."):
        try:
            response = model.generate_content(user_input)
            bot_reply = response.text

            # Store in session history
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", bot_reply))

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Show conversation history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
