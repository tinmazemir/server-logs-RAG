## -- MANIPULATE LOGS -- ##
#{62.149.159.54 - - [21/Jul/2024:10:35:33 +0000] "POST /contact HTTP/1.1" 502 4400 - Edge/90.0.818.62}
import os
import geoip2.database
from pyparsing import Word, nums, alphas, Combine, Suppress, QuotedString, Regex, oneOf, restOfLine
from datetime import datetime

DATA_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data')
GEOLOC_DATA = geoip2.database.Reader(os.path.join(DATA_FOLDER, 'GeoLite2-City.mmdb'))

def define_log_pattern():
   ipAddress = Combine(Word(nums) + '.' + Word(nums) + '.' + Word(nums) + '.' + Word(nums))
   dash = Suppress('-')
   timeStamp = Combine(Suppress('[') + Word(nums) + '/' + Word(alphas) + '/' + Word(nums) + ':' +
                    Word(nums) + ':' + Word(nums) + ':' + Word(nums) + Suppress(' ') + Word('+-', exact=1) +
                    Word(nums) + Suppress(']'))
   method = oneOf("GET POST PUT DELETE HEAD")
   url = Word(alphas + "/" + "." + "-" + "_")
   protocol = Combine(Word(alphas) + '/' + Word(nums) + '.' + Word(nums))
   statusCode = Word(nums)
   responseSize = Word(nums)
   userAgent = restOfLine

   global logPattern
   logPattern = (
      ipAddress("ip") +
      dash +
      dash +
      timeStamp("timestamp") +
      QuotedString('"')("request") +
      statusCode("status_code") +
      responseSize("response_size") +
      dash +
      userAgent("user_agent")
   )

def parse_log(logEntry):
   global logPattern
   parsedLog = logPattern.parseString(logEntry)
   '''
      print(f"IP Address: {parsedLog.ip}")
      print(f"Timestamp: {parsedLog.timestamp}")
      print(f"Request: {parsedLog.request}")
      print(f"Status Code: {parsedLog.status_code}")
      print(f"Response Size: {parsedLog.response_size}")
      print(f"User Agent: {parsedLog.user_agent}")
   '''
   return parsedLog

def enrich_metadata(parsedLogEntry, geolocData=GEOLOC_DATA):
   metadata = {"country": '', "city": '', "errorCategory": '', "timeOfDay": ''}
   ## Geolocation
   try:
      response = geolocData.city(parsedLogEntry.ip)
      metadata['country'] = response.country.name
      metadata['city'] = response.city.name
   except:
      metadata['country'] = 'Unknown'
      metadata['city'] = 'Unknown'
   ## Error Categories
   if 400 <= int(parsedLogEntry.status_code) < 500:
      metadata['errorCategory'] = "Client Error"
   elif 500 <= int(parsedLogEntry.status_code) < 600:
      metadata['errorCategory'] = "Server Error"
   else:
     metadata['errorCategory'] = "Other"
   ## User Agent

   ## Time of Day
   hour = datetime.strptime(parsedLogEntry.timestamp, '%d/%b/%Y:%H:%M:%S%z').hour
   if 5 <= hour < 12:
      metadata['timeOfDay'] =  "Morning"
   elif 12 <= hour < 17:
      metadata['timeOfDay'] =  "Afternoon"
   elif 17 <= hour < 21:
      metadata['timeOfDay'] =  "Evening"
   else:
      metadata['timeOfDay'] =  "Night"
   return metadata

def integrate_log_as_txt(parsedLogEntry, metadata):
   #Combine logs with metadata
   enrichedText = (
   f"Request from IP {parsedLogEntry['ip']} in {metadata['city']}, {metadata['country']} "
   f"on {parsedLogEntry['timestamp']} {metadata['timeOfDay']} using this agent {parsedLogEntry['user_agent']} "
   f"for {parsedLogEntry['request']} returned status {parsedLogEntry['status_code']} "
   f"({metadata['errorCategory']}) with response size {parsedLogEntry['response_size']}. "
   )
   return enrichedText