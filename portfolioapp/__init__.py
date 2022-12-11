from flask import Flask
from flask_mail import Mail

myapp = Flask(__name__,instance_relative_config=True)

myapp.config.from_pyfile("config.py")

mail = Mail(myapp)

from portfolioapp import routes