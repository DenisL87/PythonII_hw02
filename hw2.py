from flask import Flask, request
from faker import Faker
import re
import csv
import requests

app = Flask(__name__)
fake = Faker()

@app.route('/')
def home():
    return ''

@app.route('/requirements/')
def req_func ():
    with open('requirements.txt', 'r') as file:
        text = file.read()
        print(text)
    return text

@app.route('/generate-users')
def gen_users ():
    count = request.args.get('count')
    users = {}
    newdict = {}
    whilecount = 0
    while whilecount < 100:
        name = fake.name()
        email = name + '@gmail.com'
        if ' ' in email:
            email = email.replace(' ', '')
        users[whilecount + 1] = ['name: ' + name + ', email: ' + email]
        whilecount += 1
    whilecount = 0
    while whilecount < int(count):
        newdict[whilecount + 1] = users[whilecount + 1]
        whilecount += 1
    return newdict

@app.route('/mean/')
def mean():
    with open('hw.csv', 'r') as file:
        text = file.read()
    text = re.split(',|\n', text)
    heightCount = 4
    totalHeight = 0
    count = 0
    while heightCount < len(text):
        if text[heightCount] != '':
            totalHeight += float(text[heightCount])
            count += 1
        heightCount += 3
    meanheight = (totalHeight / count) * 2.54

    weightCount = 5
    totalWeight = 0
    count = 0
    while weightCount < len(text):
        if text[weightCount] != '':
            totalWeight += float(text[weightCount])
            count += 1
        weightCount += 3
    meanweight = (totalWeight / count) / 2.20462
    return f'mean height is {meanheight} cm, mean weight is {meanweight} kg'

@app.route('/space/')
def astronauts_No():
    r = requests.get('http://api.open-notify.org/astros.json')
    dict = eval(r.text)
    value = 0
    for key in dict:
        if key == 'number':
            value = dict[key]
    return str(value)

if __name__ == '__main__':
    app.run(debug=True)