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

@app.errorhandler(404)
def page_not_found(error):
	return 'Page not found', 404

if __name__ == '__main__':
    app.run()