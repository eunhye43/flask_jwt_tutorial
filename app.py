from flask import Flask
from flask_jwt_extended import *

application = Flask(import_name = __name__)
application.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "I'M IML"
		)
jwt = JWTManager(application)

@application.route("/")
def test_test():
	return "<h1>Hello, I'm IML!</h1>"

if __name__ == '__main__':
	application.run(host = '0.0.0.0',
					port = 5000, 
					debug = True)