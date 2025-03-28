from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f'<h1>Username: {username}, Password: {password}</h1>'
    
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    return file.read().decode()


if __name__ == '__main__':
    app.run(debug=True)