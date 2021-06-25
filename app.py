import os
from flask import Flask
from utils import do_this
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():

	text = 'Hi, how are you! <br> You can route to the app by adding /name/<your name> at the end of the URL <br> Give it a try!!'

	return text

@app.route('/name/<x>')
def name(x):

	do_this(x)

	filename = os.getcwd()+'/datamatrix_test_'+x+'.png'

	output = {"output":"Hi, "+x+". <br> Below is the path to your 3D barcode. <br> ",
				"path": filename
			}
	return jsonify(output)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5050))
	app.run(host='0.0.0.0', port = port, debug=True)
