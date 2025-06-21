from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader=DirectoryLoader(
    path='document_loaders/text_files',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

## we can use lazyload() when there is more document
## so that the documents are loaded consistantly