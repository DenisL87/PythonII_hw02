from flask import Flask

app = Flask(__name__)

@app.route('/requirements')
def req_func ():
    with open('requirements.txt', 'r') as file:
        text = file.read()
        print(text)
    return text

if __name__ == '__main__':
    app.run(debug=True)