import requests 
import os 
import json

#33 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
#token 22  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
#token : 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

#token = os.environ.get("GIT_HUB")
#token = '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'
#print(token)

reponame = input ("please enter the repo name you want to create : ")

token = input('please enter your token access ')

GIT_HUB_URL = "https://api.github.com/"

headers = {"Authorization" : "token {}".format(token)}

data ={"name" : "{}".format(reponame)}

create = requests.post(GIT_HUB_URL + "user/repos" + "" , data=json.dumps(data) , headers=headers )
print(create)










""" Install Pygithub using (pip install PyGithub) to enable github APIs """