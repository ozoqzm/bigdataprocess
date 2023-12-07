# 정규 표현식
import re

email_list = ['python@mail.example.com', 'python+kr@example.com', 'python-dongduk@example.co.kr',
              'python_10@example.info', 'python.dongduk@e-xample.com', '@example.com',
              'python@example', 'python@example-com']

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

for email in email_list:
    match = re.search(pattern, email)
    if match:
        print(match.group())