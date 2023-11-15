# Repositório da API: https://github.com/digitalinnovationone/santander-dev-week-2023-api
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

'''        Extract        '''

import pandas as pd
import requests
import json
import random

#   Extraindo os id do arquivo .csv
df = pd.read_csv("Pipeline_ETL/teste.csv")
user_ids = df['UserID'].tolist()
print()
print(user_ids)
print()

def generate_news(user):
    new = pd.read_csv("Pipeline_ETL/News.csv")
    msg = new['Mensagens'].tolist()
    return msg


def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))



'''     Transform       '''

#   transformando o arquivo 
for user in users:
    msg = generate_news(user)
    numero_aleatorio = random.randint(0, 2)
    user['news'] = ({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": msg[numero_aleatorio]
    })

for user in users:
    print()
    print(user)
    print()



'''     Load       '''

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  print(response.status_code)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")