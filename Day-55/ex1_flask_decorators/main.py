from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<b>{result}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<em>{result}</em>'
    return wrapper


def make_underlined(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<u>{result}</u>'
    return wrapper

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>')

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)