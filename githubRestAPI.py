import json
import requests as rq


class Github:
    def __init__(self):
        self.api_url='https://api.github.com/users/'
        self.token='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'
    def getUser(self,username):
        self.username=username
        response=rq.get(self.api_url+username)
        self.jsonDatas=json.loads(response.text)
        print(f" username:{self.jsonDatas['login']}\n id:{self.jsonDatas['id']}\n name&surname:{self.jsonDatas['name']}\n location:{self.jsonDatas['location']}\n followers:{self.jsonDatas['followers']}\n public resporities:{self.jsonDatas['public_repos']}")
        
    def getRepos(self,username):
        self.username=username
        response3=rq.get(self.api_url+username+'/repos')
        jasonDatas_repos=json.loads(response3.text)
        print("\n")
        print("All resporities\n")
        for i in range(self.jsonDatas['public_repos']):
            print(jasonDatas_repos[i]['name'])
        
        
        
username='soykuvvetberat34'
github=Github()

res=github.getUser(username)
res2=github.getRepos(username)

