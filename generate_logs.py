import random
from shlex import join
import time
from datetime import datetime, timedelta

# 127.0.0.1 - - [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
#{"time": "17/May/2015:08:05:32 +0000", "remote_ip": "93.180.71.3","request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"}

def random_ip():
   return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_date():
   start_date = datetime.now() - timedelta(days=30)
   random_days = random.randint(0, 30)
   random_seconds = random.randint(0, 86400)
   return (start_date + timedelta(days=random_days, seconds=random_seconds)).strftime('%d/%b/%Y:%H:%M:%S +0000')

def random_method():
   return random.choice(['GET', 'POST', 'PUT', 'DELETE', 'HEAD'])

def random_url():
   return random.choice(['/index.html', '/about', '/contact', '/products', '/api/v1/data'])

def random_status():
   return random.choice([200, 201, 400, 401, 403, 404, 500, 502, 503])

def random_size():
   return random.randint(100, 5000)

def random_agent():
   return random.choice(['Mozilla/5.0', 'Chrome/90.0.4430.93', 'Safari/537.36', 'Edge/90.0.818.62'])

def generate_fake_logs(num_logs):
   logs = []
   for _ in range(num_logs):
       log_entry = f'{random_ip()} - - [{random_date()}] "{random_method()} {random_url()} HTTP/1.1" {random_status()} {random_size()} - {random_agent()}'
       logs.append(str("{"+log_entry+"}"))
   return logs

def write_logs_to_file(logs, file_name='nginx_logs.log'):
   with open(file_name, 'w') as file:
      for log in logs:
         file.write(log + "\n")

fake_logs = generate_fake_logs(100)
write_logs_to_file(fake_logs)
