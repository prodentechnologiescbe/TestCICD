import pytest
# def test_file1_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed" 
# print('Test Hello --> 1.3 Bharath')

from flask import jsonify
from flask import flash, request
from flask import Flask

app = Flask(__name__)

@app.route('/data')
def users():
	try:
		rows = [(1,'vignesh'),(2,'test')]
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

if __name__ == "__main__":
    app.run()
