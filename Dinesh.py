from flask import Flask, request
import socket
app = Flask(__name__)

@app.route('/nslookup',methods = ['post'])
def get_ip():
    try:
        data = request.get_json()
        addr1 = socket.gethostbyname_ex(f'{data["url"]}')
        print(list(addr1)[-1])
        return { "URL": "Valid",
                "IP": list(addr1)[-1]}
    except socket.gaierror:
        return {"URL":"Invalid URL",
                "IP": "Not Applicable"}

app.run(port=6444)