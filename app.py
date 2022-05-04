from flask import Flask

# create new flask instance
app = Flask(__name__)

# define starting point known as "root"
@app.route('/')
def hello_world():
    return 'Hello World'


