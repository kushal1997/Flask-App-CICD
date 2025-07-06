from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Its Noizy aka Kushal - Take1 for Gihub Actions"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
