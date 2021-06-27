import os, sys
from flask import Flask, request, render_template, jsonify, url_for
from utils import do_this
import json


app = Flask(__name__, static_url_path='/')

@app.route('/')
def index():

	text = 'Hi, how are you! <br> You can route to the app by adding /name/<your name> at the end of the URL <br> Give it a try!!'

	return text

@app.route('/name/<x>')
def name(x):

	do_this(x)

	filename = '/images/datamatrix_test_'+x+'.png'

	output = {'output':'Hi, '+x+'. <br> Below is your 3D barcode. <br> ',
				'path': filename
			}

	print(json.dumps(output), flush=True)

	return render_template("app.html", value=output)


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5050))
	app.run(host='0.0.0.0', port = port, debug=True)
	# app.run(host='127.0.0.0', port = port, debug=True)
