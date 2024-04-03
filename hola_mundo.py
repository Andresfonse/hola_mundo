# hola_mundo.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html="""
        <h2>hola</h2>
        """
        self.wfile.write(html.encode('utf-8'))

def run():
    server_address = ('', 6336)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler )
    print(f"Servidor HTTP activo en el puerto ")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
