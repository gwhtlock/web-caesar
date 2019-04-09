from flask import Flask, redirect, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Web-Caesart</title>
    <style> 
    form {
        background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px; } 
        textarea { margin: 10px 0;
                width: 540px;
                height: 120px;}
                </style>
</head>
<body>"""

page_footer = """</body>
</html>"""

form =  """<form method = 'POST'> 
        <label for = "rot">Rotate by</label>

        <input type ="text" name = "rot" value ="0"/>

        <label for = "text">Enter text</label>
        <input type = "text" name ="text" id = "textarea" />
        <input type = "submit" value = "send that thing" />
    </form>"""

@app.route("/")
def index():
    return page_header+form+page_footer

@app.route("/", methods=['POST'])
def encrypt():

    rot = int(request.form['rot'])
    text = request.form['text']
    new_string = rotate_string(text, rot)
    print(new_string)
    return """<h1>{0}</h1>""".format(new_string)



app.run()