import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Establece la respuesta HTTP 200 (OK)
        self.send_response(200)
        # Establece las cabeceras de la respuesta
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Escribe el contenido de la respuesta
        self.wfile.write(b"¡Hola Mundo desde Python!")

# Configura el servidor para que escuche en el puerto especificado
with socketserver.TCPServer(("", 9000), MyHttpRequestHandler) as httpd:
    print("Servidor activo en el puerto 9000...")
    # Ejecuta el servidor hasta que se interrumpa con Ctrl+C
    httpd.serve_forever()
