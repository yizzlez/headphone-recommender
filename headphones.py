import json
from flask import jsonify

with open('data.json') as dataFile:
    jsonData = json.load(dataFile)

def typeReccomend(data, plotpath):
    headphoneType = data['type']
    opt1 = data.get('opt1', 'null')
    opt2 = data.get('opt2', 'null')
    sig = data['sig']

    if headphoneType == 'On Ear' and opt2 == 'Open Back':
        sig = 'null'

    cans = jsonData['headphones'][headphoneType][opt1][opt2][sig]
    return jsonify(signature = sig, headphones = cans, plotpath=plotpath)