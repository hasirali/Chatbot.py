# Chatbot 
 <img width="1178" height="453" alt="{315324F4-B692-4599-B0EA-B0F1261057CE}" src="https://github.com/user-attachments/assets/5171b805-25a2-4f85-8367-20988fd3fed6" />


B# 🤖 Pro-Level Terminal Chatbot (with Memory)

A robust conversational AI interface built with **LangChain** and **Google Gemini 2.5 Flash-Lite**. Unlike basic chatbots, this version maintains a structured conversation history, allowing the AI to *remember* previous interactions and follow specific personality guidelines.

---

## ✨ Features

* **Contextual Memory**
  Uses a persistent chat history to remember names, facts, and previous context within the conversation.

* **Role-Based Messaging**
  Implements `SystemMessage`, `HumanMessage`, and `AIMessage` for clear role definition and higher model accuracy.

* **Personality Control**
  A dedicated System Message defines the bot's behavior from the start.

* **Error Handling**
  Includes try-except blocks to handle API issues or connection drops gracefully.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **LLM Framework:** LangChain
* **Model:** Google Gemini 2.5 Flash-Lite
* **Environment Management:** python-dotenv

---

## ⚙️ Setup & Installation

### 1. Project Setup

```bash
git clone https://github.com/hasirali/Langchain-GenAI-II-.git
cd Chatbot
```

### 2. Environment Activation

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install langchain-google-genai python-dotenv
```

### 4. API Configuration

Create a `.env` file in the root directory and add your API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🚀 Usage

Run your chatbot script:

```bash
python main.py
```

---

## 📌 Notes

* Make sure your `.env` file is not pushed to GitHub (add it to `.gitignore`).
* Ensure you are using a compatible Python version (3.10+ recommended).
* If you face issues with API keys, verify your environment variables are loaded correctly.

---

## 💡 Future Improvements

* Add streaming responses
* Integrate a web-based UI (React / Next.js)
* Store long-term memory in a database
* Add voice input/output

---

## 📄 License

This project is open-source and available under the MIT License.

