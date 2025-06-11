from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage 
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", 
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input=input('You: ')
    chat_history.append({"role": "user", "content": user_input})
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": result.content})
    print("AI: ",result.content)

print(chat_history)