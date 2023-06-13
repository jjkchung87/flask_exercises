from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns simple 'Welcome' message
    
    >>> welcome()
    "Welcome"    
    """
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    """Returns simple 'Welcome home' message
    
    >>> welcome_home()
    "Welcome home"   

    """
    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Returns simple 'Welcome back' message
    
    >>> welcome_home()
    "Welcome home"       
    
    """
    return "welcome back"

