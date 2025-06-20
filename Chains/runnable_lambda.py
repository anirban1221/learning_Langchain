# from langchain.schema.runnable import RunnableLambda

# def word_counter(text):
#     return(len(text.split()))

# runnable_word_counter=RunnableLambda(word_counter)
# result=runnable_word_counter.invoke('hi how are you?')
# print(result)

from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableLambda,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain.chat_models import ChatOpenAI

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

prompt1=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

def word_counter(text):
    return len(text.split())

joke_gen_chain=RunnableSequence(prompt1,model1,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_counter)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'Donald trump'})
print(result)


