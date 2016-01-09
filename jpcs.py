from flask import Flask, render_template
import os
import requests
import pickle
import datetime
from os.path import isfile
import logging

app = Flask(__name__)

access_token = os.environ['INSTAGRAM_ACCESS_TOKEN']
client_secret = os.environ['INSTAGRAM_CLIENT_SECRET']

client_id = os.environ['INSTAGRAM_CLIENT_ID']

user_id = 1901568934


@app.route("/")
def index():

    filename = 'cached/' + str(datetime.date.today()) + '.instagram'
    if isfile(filename):
        with open(filename, 'rb') as f:
            out = pickle.load(f)

    else:
        endpoint = 'https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s' % (user_id, access_token)
        print endpoint
        r = requests.get(endpoint)
        data = r.json()

        out = []

        for i in data['data']:
            out.append({'url': i['images']['standard_resolution']['url'],
                        'link': i['link'],
                        'caption': i['caption']['text']})

        with open(filename, 'wb') as f:
            pickle.dump(out, f)

    return render_template('index.html', data=out)


if __name__ == "__main__":
#    logging.basicConfig(filename='/home/james/jpcs-main/app.log', level=logging.DEBUG)
    app.run(port=8123, debug=True, host="0.0.0.0")
