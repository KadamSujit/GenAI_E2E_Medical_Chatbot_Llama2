# This file will be use to push embeddings to vectordb (Pinecone)

from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone #for storing vectordb
import pinecone
from dotenv import load_dotenv
import os


#loading env variables
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

#print(PINECONE_API_KEY)
#print(PINECONE_API_ENV)

#Extracting data from pdf
extracted_data = load_pdf("data/")

#creating chunks using our custom function
text_chunks = text_split(extracted_data=extracted_data)

#download the embedding model
embeddings = download_hugging_face_embeddings()
print(embeddings)

# #Initializing the Pinecone
# #This method is deprecated and not working anymore
# '''pinecone.init(api_key=PINECONE_API_KEY,
#               environment=PINECONE_API_ENV)'''
# #use below method to initialize Pinecone
from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("medical-chatbot")

# #Storing the embeddings to vectordb
# docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index)