from flask import render_template
from app import app

# Create routes for our app
@app.route('/')
def index():
    user_info = {
        'username': 'dyannac',
        'email': 'dyanna@codingtemple.com'
    }
    drinks = ['coffee', 'water', 'smoothies', 'tea', 'broth']
    return render_template('index.html', user=user_info, drinks=drinks)


@app.route('/posts')
def posts():
    return 'Hi this is Posts!'
