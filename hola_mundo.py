# hola_mundo.py

def generate_html():
    html_content = """
    <html>
    <head>
        <title>Hola Mundo</title>
    </head>
    <body>
        <h1>¡Hola, mundo!</h1>
    </body>
    </html>
    """
    with open('/var/www/html/hola_mundo.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_html()
