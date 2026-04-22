from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content='You are a helpful {domain} assistant.'),
    HumanMessage(content='Explain in easy english about {topic}'),
])

prompt = chat_template.invoke(domain='math', topic='calculus')
print(prompt)

# from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate([
#     ('system', 'You are a helpful {domain} expert'),
#     ('human', 'Explain in simple terms, what is {topic}')
# ])

# prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

# print(prompt)