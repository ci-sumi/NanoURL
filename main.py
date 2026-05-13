
from flask import Flask,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
import base64
#Predefined sets of characters
import string
import random
from tools.url_shortner import shorten_url_pyshorteners

# To Store the short URL and their associated URLS
url_map={}
nanourl=Flask(__name__)
#Configuring the database
nanourl.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
nanourl.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Creating the database instance
db=SQLAlchemy(nanourl)

@nanourl.route("/c")
def home():
    return "Database connected"

class User(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

    def __repr__(self):
        return f"id :{self.id}name:{self.name}"
    

 
def generate_short_url():
    characters = string.ascii_uppercase+string.ascii_lowercase
    return "".join(random.choices(characters,k=6))
    
@nanourl.route('/',methods=["GET","POST"])
def index():
    google_sh = shorten_url_pyshorteners("google.com")
    shorten_url=None
    if request.method=="POST":
        shorten_url=generate_short_url()
    return render_template("index.html",shorten_url=google_sh)

# Run the application
if __name__=='__main__':
    with nanourl.app_context():
        db.create_all()
    nanourl.run(debug=True)
