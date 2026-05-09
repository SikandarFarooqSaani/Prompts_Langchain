from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7
)

# Message from human to computer 
#AI reply of AI
# System level message i.e You are helpful assistant ask politely

messages = [
    SystemMessage(content='You are helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)