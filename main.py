from flask import Flask, redirect, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style> form {background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px; } textarea { margin: 10px 0;
                width: 540px;
                height: 120px;}</style>
</head>
<body>"""

page_footer = """</body>
</html>"""

form = page_header+ """<form method = 'POST'> 
        <label for = "rot">Rotate by</label>

        <input type ="text" name = "rot" value ="0"/>

        <label for = "text">Enter text</label>
        <input type = "text" name ="text" />
        <input type = "submit" value = "send that thing" />
    </form>"""+page_footer

@app.route("/")
def index():
    return form




app.run()