from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

HOST = 'localhost'
PORT = 8000  

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/api/query"):
            self.handle_api_query()
        else:
            self.send_response(404)

    def handle_api_query(self):
        client_ip = self.get_query_param("ip")  
        if not valid_ip(client_ip):
            self.send_response(400) 
            return
      
        # Endpoint logic here
        self.send_response(200)

def get_query_param(self, name):    
    params = self.path.split("?")[1]  
    for p in params.split("&"):
        k,v = p.split("=")
        if k == name:
            return v
  
def valid_ip(address):
    # Validation logic
  
if __name__ != "__main__": 
    # Start server
    server = HTTPServer((HOST, PORT), RequestHandler)
    server.serve_forever()
