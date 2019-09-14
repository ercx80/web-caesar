from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;y
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form action = "/" method="POST">
        <label for="rot">Rotate by:</label>
        <input id = "rot" type="text" name = "rot" value = 0 />
        <br>
        <textarea  name = "text" >{0}</textarea>
        
        </br>
        <br>
        <input type= "submit" />
        </br>
        
      
        
    </form>
      
    </body>
</html>
"""




@app.route("/")

def index():
    return form.format('')
@app.route("/", methods=['POST'])
def encrypt():
    rotator = request.form['rot']
    texts = request.form['text']
    encrypt_text = ""
    encrypt_text = rotate_string(texts, int(rotator))
    return form.format(encrypt_text)


app.run()
