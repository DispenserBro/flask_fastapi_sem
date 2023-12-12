from flask import Flask


app = Flask(__name__)


@app.route('/<string:text>/')
def len_text(text: str):
    return f'Lenght of "{text}" is: {len(text)} symbols'


if __name__ == '__main__':
    app.run(debug=True)
