from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    content = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/add" method="post">
            <label for="rot">Rotate by:
                <input type="text" name="rot" id="rot"/>
                <textarea name="text" cols="40" rows="5"></textarea>
            </label>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
    """
    return content

@app.route("/add",methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]

    rotated = rotate_string(text, int(rot))
    content = "<h1>"+rotated+"</h1>"

    return content

app.run()