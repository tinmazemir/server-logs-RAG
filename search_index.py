from cgi import test
import faiss
import numpy as np 
import json
from sentence_transformers import SentenceTransformer
from torch import dist


def read_data(jsonPath='data\enriched_logs.json',indexPath='data\index_file.index'):
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
