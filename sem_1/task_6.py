# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        {'name': 'Иван',
         'last_name': 'Иванов',
         'age' : 24},
        {'name': 'Пётр',
         'last_name': 'Петров',
         'age' : 48},
        {'name': 'Сергей',
         'last_name': 'Сидоров',
         'age' : 30},
        {'name': 'Мария',
         'last_name': 'Серова',
         'age' : 27},
    ]
    
    return render_template('table.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)