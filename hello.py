import os
import keen
from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/dashboard')    
def dashboard():
	return render_template('dashboard.html')

@app.route('/webhooks',methods=['POST'])
def webhooks():
	try:
		data = json.loads(request.data)
		keen.add_event('gh', data)
		return "OK"
	except Exception, e: 
		print e

if __name__ == '__main__':
	app.run(debug=True)