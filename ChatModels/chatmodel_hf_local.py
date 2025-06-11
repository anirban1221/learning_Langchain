from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
llm= HuggingFacePipeline.from_model_id(
    model_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,

    )

)
model=ChatHuggingFace(llm=llm)
result=model.invoke("what is the capital of India?")
print(result.content)