import os

from flask import Flask, render_template

server_dir = os.path.abspath(os.path.dirname(__file__))
client_dir = os.path.join(server_dir, '../client')
build_dir = os.path.join(client_dir, 'build')
static_dir = os.path.join(build_dir, 'static')

app = Flask(__name__, template_folder=build_dir, static_folder=static_dir)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))