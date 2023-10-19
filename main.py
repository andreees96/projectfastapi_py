from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()



@app.get('/',response_class=HTMLResponse)
def get_pagehome():
    return """
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1>¿Hola?</h1>
            <a href="/contact">Pincha aquí</a>
        </body>
    </html>
    """

@app.get('/contact',response_class=HTMLResponse)
def get_pagecontact():
    dic = {'name': 'Andres', 'phone':'+56950607983','email':'andres.mvid96@gmail.com'}
    
    html_content = """
    <html>
        <head>
            <title>Contact Page</title>
        </head>
        <body>
            <h1>Contact Information</h1>
    """
    for key, value in dic.items():
        html_content += f"<li>{key}: {value}</li>"
    html_content+="""
            <br>
            <a href='/'>Devolver</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

