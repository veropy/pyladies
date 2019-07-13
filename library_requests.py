
# coding: utf-8

# # Exemplos de uso da biblioteca requests

# ### Instalando a biblioteca
# pip install requests


# ### Importando as dependências
import requests

from pandas.io.json import json_normalize


# ## 1) Onde está a estação espacial internacional neste momento?
url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url)

r.status_code

r.json()

r.json()['iss_position']['latitude']

json_normalize(r.json()['iss_position'])


# ## 2) Imagem astronômica do seu aniversário em 2018!
url = "https://api.nasa.gov/planetary/apod"
params = {'date': '2018-12-15',
          'api_key': 'DEMO_KEY'}
r = requests.get(url, params=params)

r.status_code

r.json()['url']


# ## 3) Testando métodos com httpbin.org
url = "http://httpbin.org/post"
headers = {'Accept': 'json/application'}
params = {'date': '2019-07-13'}
data = {'name': 'PyLadies'}
r = requests.post(url, headers=headers, params=params, data=json.dumps(data))

r.status_code

r.json()

