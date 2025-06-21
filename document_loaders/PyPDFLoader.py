from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('D:\Langchain_models\document_loaders\Bayesian classifier.pdf')
docs=loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)