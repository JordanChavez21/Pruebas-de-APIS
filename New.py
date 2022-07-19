import requests
import json

class Clasesita:

    def __init__(self):
        link = 'https://login.salesforce.com/services/oauth2/token'
        params = {
            'grant_type': 'password', 
            'client_id': '3MVG9tSqyyAXNH5IQWf2trTVP3Inkla9LeTiE4NdHbOrejINDBDwOBsW367M7HXCTfcIRvJH6kiCNZdBvWnSo', 
            'client_secret': '635F1C6CD0487D0F33481E71E72D7CCC9210F5D8428F08CCF03970A8F8845A78',
            'username': 'jchavez@bafar.com.mx',
            'password': 'Inicio.2022KGo0ediHeEVmQKQRIpswbaxT6'
        }

        sessionInfo = json.loads(requests.post(link,params=params).text)
        # print(json.dumps(sessionInfo,indent=4,sort_keys=True))
        self.d = sessionInfo

    def getAllStudents(self):
        link = self.d['instance_url']+'/services/data/v49.0/sobjects/Student__c'
        aut = {'Authorization': 'Bearer '+ self.d['access_token']}
        res = json.loads(requests.get(link,headers = (aut)).text)['recentItems']
        # print(json.dumps(data,indent=4,sort_keys=True))

        for y in res:
            print(y['Id'])

    def getStudentById(self,id):   
        link = self.d['instance_url']+"/services/data/v49.0/sobjects/Student__c/"+id
        aut = {'Authorization': 'Bearer '+ self.d['access_token']}
        res =  json.loads(requests.get(link,headers = (aut)).text)
        return res

# /a018Z00000ui9PMQAY
data = Clasesita()
data.getAllStudents()
res = json.dumps(data.getStudentById('a008Z00001RLof3QAD'),indent=4,sort_keys=True)
print(res)

