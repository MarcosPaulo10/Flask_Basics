from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Arroz'
    myresult = 10 + 20
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist=mylist)

@app.route('/other')
def other():
    some_text = 'Hello, World!'
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

if __name__ == '__main__':
    app.run(debug=True)