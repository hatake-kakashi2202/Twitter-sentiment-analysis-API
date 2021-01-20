import json
import requests

from flask import Flask, request, redirect, url_for, flash, jsonify
url = 'http://127.0.0.1:5000/api/'

data = "Now, all you need to do is call the web server with the correct syntax of data points."
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)