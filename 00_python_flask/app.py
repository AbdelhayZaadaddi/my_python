from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = 'Abdelhay Zaadaddi'
    current_date = '2023-10-01'
    return render_template('index.html', name = user_name, date = current_date)

if __name__ == '__main__':
    app.run()