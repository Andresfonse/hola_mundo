from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><head><title>Hola Mundo</title></head>")
        self.wfile.write(b"<body><h1>¡Hola, mundo!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor HTTP activo en el puerto {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
