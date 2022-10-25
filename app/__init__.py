from flask import Flask

#Create an insatnce of the Flask class and give it the variable name "app"
app = Flask(__name__)

from . import routes