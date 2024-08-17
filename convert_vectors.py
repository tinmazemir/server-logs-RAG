import json
from sentence_transformers import SentenceTransformer

def read_json(file_path):
   with open(file_path, 'r') as file:
      data = json.load(file)
   file.close()
   return data

def creat_vector(text):
   model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
   text_embedding = model.encode(text)
   return text_embedding

def write_vectors_to_json(data, file_path):
   for i in range(len(data)):
      data[i]['vector'] = str(creat_vector(data[i]['log']))
      #print(data[i]['vector'])   
   with open(file_path, 'w') as file:
      json.dump(data, file,indent=2)
   file.close()

data = read_json('data\enriched_logs.json')
write_vectors_to_json(data, 'data/enriched_logs.json')
#creat_vector(read_json('data\enriched_logs.json')[0]['log'])