from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = ""

    with open("index.html","r") as f:
        html = ''.join(f.readlines());
    return html

@app.route('/subpage')
def hello_world():
    return 'Hello World!\nThis is a subpage.'

if __name__ == '__main__':
    app.run()
