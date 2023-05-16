#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install facebook


# In[6]:


pip install facebook-sdk


# In[7]:


pip install pypi


# In[3]:


pip install --upgrade python-facebook-api


# In[1]:


import facebook


# In[2]:


import json


# In[5]:


import pandas as pd


# In[6]:


graph=facebook.GraphAPI('')
posts=graph.get_object(id='',fields='comments')
print(json.dumps(posts,indent=4))
filecsv=pd.read_json(json.dumps(posts,indent=4))
filecsv.to_csv('FBcomments.csv',index=None)


# In[9]:


pip install requests


# In[20]:


import requests 


# In[12]:


import time


# In[13]:


import pickle


# In[14]:


import random


# In[15]:


token='EAAHfxwkFQuQBAOU4TY8lQFJVoQ3XLJQ1Vfs7xmwbC0sRVLR0ebAO7umZCEizE1rxNpl2ErXCwlorMFiT7bDuOlaTlYmbZC13r7Uz5HmctHl1MuM6C5EHQWS6347Vjt1rMcK5eQBrYyiWJfejT4ZAhWXGX1evS1Yqu3DZCfZCJWGecK6fh4J8ZAzP7BAyeQ70AKGDhkEN6eL0ZBMkKxFZAmIrFZALxxpejytazFJJMdUDTqw4LZANZBpXBai'


# In[19]:


https:


# In[21]:


import requests

app_id = '527520919536356'  # Replace with your own app ID
app_secret = '71760b4a764d0509b24cfa722f46c1eb'  # Replace with your own app secret
short_lived_token = 'EAAHfxwkFQuQBAPJyhPifb2DtXUNZCLl04KctAVeTG5EakK5II9f7JxSX4ehkk9vsKFnzsZBsIwTJqO0xQOPpJrPNZB92bvRJVXZC3EiBxmoQ5uhZCjqPZCiA6ajRiCmIZAeiZAMXC871ycZAL8EGh0klczdHOzd8LeVf5YrXTZAirR80752c6uPnbDG2ONLQXVmnBaVVpARK6i3HoMsjraDiCGYe6KQBkGXlG6yBdnk2iZBxGNvPCJOEZBsJ'  # Replace with your own short-lived access token

url = f'https://graph.facebook.com/v12.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_lived_token}'
response = requests.get(url)

long_lived_token = response.json()['access_token']


# In[62]:


import requests


post_id = '02Ftf8YdWw2DDZh2Ui8Res62bM2JgCpRvX4efuq531SCNnUrzUNcGFk2M8NJDGF7dhl'  
# Replace with the ID of the post you want to parse comments from
access_token = 'EAAHfxwkFQuQBABLZBBmNIYNTO8zBIL0A31tYF35VtW4bLCisMji8FIPvZA1HTex2nLiGrWYQUPSn4UcPYHLG1pZBo5Cr3nulDN49ZAxeH7kOrxYnj96UoovlF2ZA2o9L28FhCilXeuX7lKvJ4FprhlsiD210DrcgQOWsA7yaRyNThtClRFdZCnaxygZBrS3qhpxzGnMe16fGakLtXHr0r0k'
url = f'https://graph.facebook.com/v12.0/{post_id}/comments?access_token={access_token}'


# In[63]:


url = f'https://graph.facebook.com/v12.0/{post_id}/comments?access_token={access_token}'
response = requests.get(url)


# In[64]:


response = requests.get(url)


# In[66]:



# Parse the JSON response into a Python object
data = json.loads(response.text)

comments = response.json()


# In[59]:


import json


# In[67]:


print(json.dumps(data, indent=2))


# In[60]:


comments = response.json()['data']


# In[61]:


# Parse the JSON response into a Python object
data = json.loads(response.text)

# Print the entire JSON response
print(json.dumps(data, indent=2))


# In[68]:


page_id='100091921387756'


# In[69]:


post_id='105133019227411'


# In[70]:


access_token='EAAHfxwkFQuQBAKR5LLRyXyotlRblt7DT4eQLCXMYoY1tHusFvzjDgh97JgfJ0rE2RfEea0W4z9i3HbByofe6cBcm9iofAPpzVZBXbHZBLN3pcS5htZBlO27ENacI0qvIwuB7sB5uZAovC92FmgnBSwvWgeob5wvhS7pXCjGmu6EHRsOwCKCy'


# In[71]:


url = f'https://graph.facebook.com/v12.0/{page_id}_{post_id}/comments?access_token={access_token}'


# In[81]:


response = requests.request("GET", url)

# save name, time, message in excel file
data = json.loads(response.text)

# create object with only name, time, message
def get_comment(comment):
    return {
        'name': comment['from']['name'],
        'time': comment['created_time'],
        'message': comment['message']
    }

excel_data = list(map(get_comment,data["data"]))
df = pd.DataFrame(excel_data)
df.to_excel('comments.xlsx', index=False)


# In[ ]:





# In[82]:


import requests
import pandas as pd
import json

page_id = '100091921387756' # your page id, ex: '123456789'
post_id = '105133019227411' # your post id, ex: '123456789'
access_token='EAAHfxwkFQuQBAKR5LLRyXyotlRblt7DT4eQLCXMYoY1tHusFvzjDgh97JgfJ0rE2RfEea0W4z9i3HbByofe6cBcm9iofAPpzVZBXbHZBLN3pcS5htZBlO27ENacI0qvIwuB7sB5uZAovC92FmgnBSwvWgeob5wvhS7pXCjGmu6EHRsOwCKCy'
url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

response = requests.request("GET", url)

# save name, time, message in excel file
data = json.loads(response.text)

# create object with only name, time, message
def get_comment(comment):
    return {
        'name': comment['from']['name'],
        'time': comment['created_time'],
        'message': comment['message']
    }

excel_data = list(map(get_comment, data[data']))
df = pd.DataFrame(excel_data)
df.to_excel('comments.xlsx', index=False)


# In[84]:


import requests
import pandas as pd
import json

page_id = '100091921387756'
post_id = '105133019227411'
access_token='EAAHfxwkFQuQBAAH9tF0FDKuQhyYLIBVHO689ZAyYwXkhF9KaDyWXporjRZA9ffdmukFiLtbwJWlekVa0x86Ol41sl1fywSOt6S9a7sqEZBGfOPudsqZBqYtsXpPjzqfvjUSLNZBGprBamZCn9WObPW9wFLAO6JTbay3Jd35V7cwNS1HmMYOjRW4gZCLPKeLfctrNRkZBhVLUh8qiM5PLPqBCF7D2MC6nJd3Qqw3ZBmx6agZAZACmcS8kv6C'
url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

response = requests.request("GET", url)

# Print the entire JSON response
print(json.dumps(json.loads(response.text), indent=2))


# In[ ]:




