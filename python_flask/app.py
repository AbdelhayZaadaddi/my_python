from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

# Try to create more then one route

@app.route('/contact')
def contact():
    return 'Contact us from here!'

@app.route('/home')
def home():
    return 'This is the home page!'

if __name__ == '__main__':
    app.run()