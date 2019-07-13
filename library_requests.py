
# coding: utf-8

# # Exemplos de uso da biblioteca requests

# ### Instalando a biblioteca

# In[ ]:


get_ipython().system(u'pip install requests')


# ### Importando as dependências

# In[7]:


import requests

from pandas.io.json import json_normalize


# ## 1) Onde está a estação espacial internacional neste momento?

# In[14]:


url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url)


# In[15]:


r.status_code


# In[16]:


r.json()


# In[18]:


r.json()['iss_position']['latitude']


# ## 2) Imagem astronômica do seu aniversário em 2018!

# In[94]:


url = "https://api.nasa.gov/planetary/apod"
params = {'date': '2018-12-15',
          'api_key': 'DEMO_KEY'}
r = requests.get(url, params=params)


# In[92]:


r.status_code


# In[95]:


r.json()['url']


# ## 3) Testando métodos com httpbin.org

# In[89]:


url = "http://httpbin.org/post"
headers = {'Accept': 'json/application'}
params = {'date': '2019-07-13'}
data = {'name': 'PyLadies'}
r = requests.post(url, headers=headers, params=params, data=json.dumps(data))


# In[96]:


r.status_code


# In[90]:


r.json()

