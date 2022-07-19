from flask import  Flask, request, make_response, jsonify
import requests
import json
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

url = 'https://svgwdap0.grupobafar.com:8443'
cf_port = os.getenv("PORT")
user = 'PUBLIC_NODE'
password = 'Sistemas01'

def get_request(base_url, headers):
    r = requests.get(base_url ,headers=headers, auth=(user,password),verify=False) 
    data = json.loads(r.text)
    return data

@app.route('/webhook/GetInfo',methods=['GET'])
@cross_origin()
def webhook():
  
    if (request.method == 'GET'):
        base_url = url+"/neptune/api/CONSULTA/ZONAS"
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        pos_data=get_request(base_url,headers)
        print(pos_data)
        return jsonify(pos_data)


if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=True)