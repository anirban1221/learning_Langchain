from langchain_community.document_loaders import WebBaseLoader
url='https://en.wikipedia.org/wiki/Cristiano_Ronaldo'
loader=WebBaseLoader(url)
docs=loader.load()

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence
import os

# Load .env
load_dotenv()
groq_token = os.getenv("GROQ_API_KEY")

# Set base URL for Groq (OpenAI-compatible)
groq_base_url = "https://api.groq.com/openai/v1"

# Model 1: Mixtral-8x7B (via Groq)
model1 = ChatOpenAI(
    openai_api_key=groq_token,
    openai_api_base=groq_base_url,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)
prompt=PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)
parser=StrOutputParser()

chain=prompt|model1|parser

result=chain.invoke({'question':"How many Ballon'dors Christiano Ronaldo won?","text":docs[0].page_content[:10000]})
print(result)
