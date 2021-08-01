from flask import Flask

app = Flask(__name__)

@app.route('/requirements')
def req_func ():
    with open('requirements.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(debug=True)