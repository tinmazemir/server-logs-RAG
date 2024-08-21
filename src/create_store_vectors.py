## -- CREATE & STORE  VECTORS -- ##
import os
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

DATA_FOLDER = data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')

def create_vector(text):
   model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
   text_embedding = model.encode(text)
   return text_embedding

def save_indexs(vectors,path= os.path.join(DATA_FOLDER, 'index.index')):
   vectors = np.array(vectors).astype('float32')
   dimension = vectors.shape[1]
   index = faiss.IndexFlatL2(dimension)
   index.add(vectors)
   faiss.write_index(index, path)

