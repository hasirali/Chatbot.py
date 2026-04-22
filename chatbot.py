from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

chat_history = []

while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    result = model.invoke(chat_history + [user_input])
    chat_history.append(user_input)
    chat_history.append(result.content)
    print("Bot: ",  result.content)