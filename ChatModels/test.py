import langchain
import os
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="D:/langchain_models/.env")

print(langchain.__version__)
print("Token loaded:", os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))
