# template.py is used to create project sturcture in terms of files and folders.
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#listing required files and folders
list_of_files = [
    "src/__init__.py", #source folder with its constructor __init__.py. (wherever __init__.py file is present, that particular folder is considerd as a package)
    "src/helper.py", #helper functions
    "src/prompt.py", 
    ".env", #for storing environment variables
    # "requirements.txt" #for installing required libs
    "setup.py", #for setting up project
    "research/trials.ipynb", # for experimenting with notebook
    "app.py", # appplication file for running flask app
    "store_index.py", #
    "static/.gitkeep",
    "templates/chat.html"

]

for filepath in list_of_files:
   filepath = Path(filepath) #converting to path variable.
   filedir, filename = os.path.split(filepath) #seperating files and folders from path
   
    # if filedir not empty, create that dir
   if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")
    
    # if file from listoffiles does not exists in dir of if its size is zero then create new file.   
   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
       with open(filepath, 'w') as f: #creating empty file
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    # if file already exists
   else: 
        logging.info(f"{filename} is already created")
      