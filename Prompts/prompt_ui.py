from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st 

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", 
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)


st.header('Research Tool')
paper_input=st.selectbox("Select Research paper Name",["Select...","Attention is All you Need",
                                                       "BERT:Pre-training of Deep Bidirectional transformers",
                                                        "GPT-3:Language Models are Few shot learners","Diffusion Models Beat GANs on Image Syntesis"])

style_input=st.selectbox("Select explanation Style",["Begginer-friendly", "technical", "Code-Oriented", "Mathematical"])

length_input=st.selectbox("select Explanation style",["Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(detailed explanation)"])

## template
template=PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style:{style_input}
Explanation Length:{length_input}
1.Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
- Use relatable analogies to simplify complex ideas.
if certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
ensure the summary is clear, accurate, and aligned with aligned with the provided style and length.
""",
input_variables=['paper_input','style_input','length_input']
)

prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})



if st.button('Summarize'):
    result=model.invoke(prompt)
    st.write(result.content) 

