import os
import generate_logs 
import manipulate_logs
import create_store_vectors
import json



def generate(quantity):
   allData = []
   enrichedLogs = []
   vectors = []
   manipulate_logs.define_log_pattern()
   logs = generate_logs.generate_fake_logs(quantity)
   for log in range(len(logs)):
      parsedLog = manipulate_logs.parse_log(logs[log].strip("{}"))
      enrichedMetadata = manipulate_logs.enrich_metadata(parsedLog, manipulate_logs.GEOLOC_DATA)
      integratedLog= manipulate_logs.integrate_log_as_txt(parsedLog, enrichedMetadata)
      vector = create_store_vectors.create_vector(integratedLog)
      enrichedLogs.append(integratedLog)
      vectors.append(vector)
   create_store_vectors.save_indexs(vectors)
   with open(os.path.join(manipulate_logs.DATA_FOLDER,'enriched_logs2.json'), 'w') as file:
      for i in range(len(logs)):
         data={
            "id": i,
            "log": enrichedLogs[i],
            "vector":str(vectors[i].tolist())
         }
         allData.append(data)
      json.dump(allData, file, indent=4)


generate(10)