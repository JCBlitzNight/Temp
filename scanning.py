import socket
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/api/query')
def api_query():
    client_ip = request.args.get('ip')
    file_path = request.args.get('filepath')
    
    if not valid_ip(client_ip): 
        return "Invalid IP", 400
    
    real_path = valid_file_path(file_path)
    if not real_path:
        return "Invalid file path", 400 

    # API logic here 

    return "OK"

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True 
    except:
        return False

def valid_file_path(path):
    real_path = os.path.realpath(path)  
    if real_path.startswith("/"):
        return False     
    return real_path  
