from flask import Flask

# Web Development with Python Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Muhammad Kaleem!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



