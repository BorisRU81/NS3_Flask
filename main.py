from flask import Flask #какркас вариант Flask приложения

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Privet!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

я