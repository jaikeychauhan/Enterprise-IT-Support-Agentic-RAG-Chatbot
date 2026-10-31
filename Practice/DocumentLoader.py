from langchain_core.documents import Document
data = Document(
    page_content='This article is for learning all ' \
    'about the Document Loader in LangChain/AI',
    id=1,
    metadata={'source': 'Web'}
)
print("Data: ",data)
print("Page Content: ",data.page_content)