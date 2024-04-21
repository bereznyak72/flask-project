from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', title='Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/soup')
def soap():
    return render_template('soup.html', title='Рецепт супа')


@app.route('/croissant')
def croissant():
    return render_template('croissant.html', tittle='Рецепт круассана')


@app.route('/')


@app.route('/bread')
def bread():
    return render_template('bread.html', title='Рецепт хлеба')


@app.route('/borsch')
def borsch():
    return render_template('borsch.html', title='Рецепт борща')


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
