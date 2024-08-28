#todo: yet to be finalised

# import openai
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.document_loaders import TextLoader
# from langchain.vectorstores import SimpleVectorStore
#
# from .models import Document
#
# openai.api_key = 'your-openai-api-key'
#
# # Load and process documents
# def load_documents():
#     documents = Document.objects.all()
#     text = "\n".join(doc.file.read().decode('utf-8') for doc in documents)
#     return text
#
#
# def create_chatbot():
#     text = load_documents()
#     text_splitter = CharacterTextSplitter()
#     texts = text_splitter.split(text)
#
#     embeddings = OpenAIEmbeddings()
#     vectorstore = SimpleVectorStore.from_texts(texts,embeddings)
#
#     retriever = vectorstore.as_retriever()
#     qa_chain = RetrievalQA.from_chain_type(
#         retriever = retriever,
#         chain_type='stuff',
#         llm=OpenAIEmbeddings()
#     )
#     return qa_chain
#
#
# def get_chatbot_response(query):
#     chatbot = create_chatbot()
#     response = chatbot.run(query)
#
#     return response