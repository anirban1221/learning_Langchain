from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('document_loaders/text_files/Deep Learning Curriculum (1).pdf')
docs=loader.load()
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_documents(docs)
print(result[0].page_content)