from time import sleep
import openai as OpenAI
from API_KEYS import *
import search_index as search_index


def define_openai_key():
   global OpenAI
   OpenAI.api_key = OPENAI_API_KEY


def get_chatgpt_response(logs =list,question= str):
   logText = ""
   for i in range(len(logs)):
      logText += str(str(i+1)+"-> "+logs[i])
   global OpenAI
   #print(logText)
   #print(question)
   try:
      response = OpenAI.chat.completions.create(
         model="gpt-4o-mini",
         messages=[
            {"role": "system", "content": "You are a server log analyser assistan. You should answer questions with data given to you with technical terms."},
            {"role": "system", "content": "The data is "+logText},
            {"role": "user", "content": "Generate answer for the following question: "+question},
         ],
      )
   except OpenAI.RateLimitError:
      print("You have reached the rate limit for OpenAI API.")
      print(OpenAI.RateLimitError)
      sleep(60)
      return get_chatgpt_response(logs,question)
   return response

