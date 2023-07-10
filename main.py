from flask import Flask, url_for #какркас вариант Flask приложения

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Адмирал! <br><a href="/slogan"> А слоган к фильму есть ? <a/>'

@app.route('/slogan')
def slogan ():
    return 'Ибо крепка, как смерть, любовь!<br><a href = "/"> А какое было название фильма? </a>'

@app.route('/countdown')   #Декоратор. Функции пишем через декоратор.
def countdown():
    lst=[str(x) for x in range(10, 0, -1)]
    lst.append('Start!!! puuuffffff')
    return '<br>'.join(lst)

@app.route('/poster')  # Добавление картинки через HTML
def poster ():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poster</title>
    <link rel="stylesheet" type:"text/css" href= {url_for('static', filename='css/style.css')}>
</head>
<body>
<h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/Japan.jpg')}"
alt="Тут должна была быть картинка но она не прогрузилась. Печаль.">

<p> И спать охота, что п*****</p>
</body>
</html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

