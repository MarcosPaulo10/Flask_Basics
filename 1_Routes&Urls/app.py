from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá, tudo certo?</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'<h1>Result: {int(number1) + int(number2)}</h1>'

@app.route('/handle_url_params')
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'<h1>{greeting}, {name}!</h1>'
    else:
        return '<h1>Missing greeting or name parameter</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555', debug=True)