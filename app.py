from flask import Flask
app = Flask(__name__)


@app.route('/')
def helloWorld():
    return'<h1>Hello!</h1>'


@app.route('/info')
def info():
    return'<h1>Hello world !</h1>'


if __name__ == '__main__':
    app.run()
