#! run.py

import requests, json, traceback, sys
from flask import Flask, request, jsonify
from config import URL_API, KEY_TOKEN

app = Flask(__name__)

def msg_error(code, msg):
    output = {
        'code' : code,
        'message' : msg
    }
    return jsonify(output)

@app.route("/longShortUrl")
def longShortUrl():
    try:
        longUrl = request.args.get('longUrl')
        urlApi = '%s?alt=json&key=%s' % (URL_API, KEY_TOKEN)
        payload = {'longUrl': longUrl}
        headers = {'Content-type': 'application/json'}
        req = requests.post(urlApi, data=json.dumps(payload), headers=headers)
        data = json.loads(req.text)
        if data.get('id'):
            return jsonify(data)
        else:
            return msg_error(404, 'not found')
    except Exception as e:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, str(e))

@app.route("/shortLongUrl")
def shortLongUrl():
    try:
        shortUrl = request.args.get('shortUrl')
        urlApi = '%s?alt=json&shortUrl=%s&key=%s' % (URL_API, shortUrl, KEY_TOKEN)
        headers = {'Content-type': 'application/json'}
        req = requests.get(urlApi, headers=headers)
        data = json.loads(req.text)
        if data.get('id'):
            return jsonify(data)
        else:
            return msg_error(404, 'not found')
    except Exception as e:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, str(e))
        
@app.route("/analytics")
def analytics():
    try:
        shortUrl = request.args.get('shortUrl')
        urlApi = '%s?alt=json&shortUrl=%s&key=%s&projection=FULL' % (URL_API, shortUrl, KEY_TOKEN)
        headers = {'Content-type': 'application/json'}
        req = requests.get(urlApi, headers=headers)
        data = json.loads(req.text)
        if data.get('id'):
            return jsonify(data)
        else:
            return msg_error(404, 'not found')
    except Exception as e:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, str(e))

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
