from langchain.document_loaders import PyPDFLoader, DirectoryLoader #for pdf and dir loading
from langchain.text_splitter import RecursiveCharacterTextSplitter #for creating chunks
from langchain.embeddings import HuggingFaceEmbeddings #for creating embeddings




#loading data
#Extracting data from pdf
def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf", #loads all pdf files from thd directory
                    loader_cls=PyPDFLoader) #lodar class is PyPDFLoader to load the pdfs
    documents = loader.load()
    return documents


#Creating text chunks from extracted data
#creating custom function to create chunk from input data
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)
    
    return text_chunks

#download the embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

