from flask import Flask #какркас вариант Flask приложения

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Адмирал! <br><a href="/slogan"> Слоган <a/>'

@app.route('/slogan')
def slogan ():
    return 'Ибо крепка, как смерть, любовь!<br><a href = "/"> Назад</a>'

@app.route('/countdown')   #Декоратор. Функции пишем через декоратор.
def countdown():
    lst=[str(x) for x in range(10, 0, -1)]
    lst.append('Start!!! puuuffffff')
    return '<br>'.join(lst)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

