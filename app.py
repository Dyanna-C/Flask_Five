from flask import Flask

#Create an insatnce of the Flask class and give it the variable name "app"
app = Flask(__name__)

#Create a rooute usin the @app.route to trigger function base don endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'


#add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'

#add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'