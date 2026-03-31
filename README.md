# 💬 Gemini AI ChatBot

A powerful, interactive, and seamless conversational AI web application built using **Python**, **Streamlit**, and the latest **Google Gemini 2.0 Flash Model**. 

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## ✨ Features

- **Blazing Fast Responses:** Powered by `gemini-2.0-flash` for high-quality, real-time AI generation.
- **Conversational Memory:** Preserves your chat history across the session for continuous context.
- **Elegant & Simple UI:** Built on Streamlit to ensure a clean, modern, and highly responsive user interface.
- **Secure Integration:** Utilizes environment variables securely via `python-dotenv` for API key protection.

## 🚀 Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites

Make sure you have Python 3.8+ installed on your machine.
You will also need a **Google Gemini API Key**. You can grab one from [Google AI Studio](https://aistudio.google.com/).

### Installation

1. **Clone the repository** (or download the source files):
   ```bash
   git clone https://github.com/hrshjswniii/ChatBot.git
   cd ChatBot
   ```

2. **Install the required packages:**
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```

3. **Set up the Environment Variables:**
   - Create a new file named `.env` in the root directory.
   - Add your Gemini API key like so:
   ```env
   google_api=YOUR_API_KEY_HERE
   ```

### Running the App

Start the Streamlit development server by running:

```bash
streamlit run chatbot_app.py
```

The application will automatically pop up in your default web browser at `http://localhost:8501`.

## 📁 Repository Structure

- `chatbot_app.py` - The core application script containing Streamlit UI and Gemini Logic.
- `.env` - Environment file (not included in the repository) that holds the API key safely.

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** - The fastest way to build data apps in Python.
- **[Google Generative AI](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview)** - For integrating Gemini large language models.
- **[Dotenv](https://pypi.org/project/python-dotenv/)** - For handling environment configuration securely.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/hrshjswniii/ChatBot/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Made with ❤️ by [Harsh Jeswani](https://github.com/hrshjswniii)*
