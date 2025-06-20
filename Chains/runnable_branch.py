from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableLambda,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain.chat_models import ChatOpenAI

-