# hola_mundo.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mi Página Web</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                p {
                    line-height: 1.6;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenido a Mi Página Web</h1>
                <p>Esta es una página web simple creada con Python y el módulo http.server.</p>
                <p>Aquí puedes agregar más contenido según tus necesidades y preferencias.</p>
                <p>¡Disfruta explorando!</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

def run():
    server_address = ('', 6336)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Servidor HTTP activo en el puerto {server_address[1]}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
