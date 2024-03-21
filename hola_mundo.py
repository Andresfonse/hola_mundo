from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

# Cambia el directorio raíz del servidor HTTP al directorio donde se encuentra el archivo HTML
SimpleHTTPRequestHandler.extensions_map.update({
    '.html': 'text/html',
})

# Ejecuta el servidor HTTP en el puerto 80
server_address = ('', 80)
httpd = HTTPServer(server_address, MyHTTPRequestHandler)
print('Servidor HTTP activo...')
httpd.serve_forever()
