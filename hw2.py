from flask import Flask
from faker import Faker
import re
import csv

app = Flask(__name__)
fake = Faker()

@app.route('/requirements')
def req_func ():
    with open('requirements.txt', 'r') as file:
        return file.read()

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
        heightCount += 2
    meanheight = totalHeight / count

    weightCount = 5
    totalWeight = 0
    count = 0
    while weightCount < len(text):
        if text[weightCount] != '':
            totalWeight += float(text[weightCount])
            count += 1
        weightCount += 2
    meanweight = totalWeight / count
    return f'mean height is {meanheight}, mean weight is {meanweight}'

if __name__ == '__main__':
    app.run(debug=True)