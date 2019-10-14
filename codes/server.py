from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 33507))


@app.route('/', methods=['POST'])
def index():
  
  data = json.loads(request.get_data())


  crypto_name = data["nlp"]["entities"]["crypto_name"][0]["raw"]
  crypto_ticker = crypto_name.upper()


  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_ticker+"&tsyms=BTC,USD,EUR")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'The price of %s is :\n%f BTC, \n%f USD, and \n%f EUR.' % (crypto_ticker, r.json()['BTC'], r.json()['USD'], r.json()['EUR'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")