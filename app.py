from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone #for storing vectordb
import pinecone
from langchain.prompts import PromptTemplate #for prompting
from langchain.chains import RetrievalQA #for retrieving ans
from langchain.llms import CTransformers #quantized model
from dotenv import load_dotenv
from src.prompt import *
import os

#initialize flask obj
app = Flask(__name__)

#loading env variables
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# #download the embedding model
# embeddings = download_hugging_face_embeddings()

# # #Initializing the Pinecone
# # #This method is deprecated and not working anymore
# # '''pinecone.init(api_key=PINECONE_API_KEY,
# #               environment=PINECONE_API_ENV)'''
# # #use below method to initialize Pinecone
# from pinecone import Pinecone, ServerlessSpec
# pc = Pinecone(api_key=PINECONE_API_KEY)
# index = pc.Index("medical-chatbot")
# # # loading embeddings from existing index
# # docsearch=Pinecone.from_existing_index(index_name=index, embeddings)


# #designing prompt and chaining it
# PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
# chain_type_kwargs={"prompt": PROMPT}
# #loading llm model
# llm=CTransformers(model="model\llama-2-7b-chat.ggmlv3.q4_0.bin",
#                   model_type="llama",
#                   config={'max_new_tokens':512,
#                           'temperature':0.8})

# #initialize QA bot
# qa=RetrievalQA.from_chain_type(
#     llm=llm, 
#     chain_type="stuff", 
#     retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
#     return_source_documents=True, 
#     chain_type_kwargs=chain_type_kwargs)


#routing to home html for chatting
@app.route("/")
def index():
    return render_template('chat.html')


# #routing for chatting with qa bot (RetrievalQA)
# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     result=qa({"query": input})
#     print("Response : ", result["result"])
#     return str(result["result"])

 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
