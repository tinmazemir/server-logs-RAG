from cgi import test
import faiss
import os 
import numpy as np 
import json
from sentence_transformers import SentenceTransformer
from torch import dist

DATA_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data')

def read_data(jsonPath=os.path.join(DATA_FOLDER, 'enriched_logs.json'),indexPath=os.path.join(DATA_FOLDER, 'index.index')):
   with open(jsonPath, 'r') as file:
      jsonData = json.load(file)
   file.close()
   index = faiss.read_index(indexPath)
   return jsonData, index

def search_index(searchText, index, k=1):
   index = index
   model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
   vector = model.encode(searchText)
   vector = np.array(vector).astype('float32')
   vector = np.array(vector).reshape(1, 384) 
   distance, indices = index.search(vector, k)
   return distance, indices

def log_finder_from_index(indices,jsonData):
   indices= indices.tolist()
   relatedLogs = []
   for index in indices[0]:
      relatedLogs.append(jsonData[index]['log'])
   return relatedLogs
