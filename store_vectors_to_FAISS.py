from cgi import test
import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer



def read_json(json_file):
   logs = []
   vectors = []  
   with open(json_file, 'r') as f:
      data = json.load(f)

   for i in range(len(data)):
      logs.append(data[i]['log'])
      vectorSTR = data[i]['vector']
      vector= np.fromstring(vectorSTR[1:-1], sep=' ')
      vectors.append(vector)
   
   return logs, vectors

def save_indexs():
   global logs, vectors
   logs, vectors = read_json('data/enriched_logs.json')
   logs = np.array(logs)
   vectors = np.array(vectors).astype('float32')
   #print(vectors.shape)
   dimension = vectors.shape[1]
   index = faiss.IndexFlatL2(dimension)
   index.add(vectors)
   faiss.write_index(index, "data\index_file.index")

