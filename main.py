
import datetime

from flask import Flask, app,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
import base64
#Predefined sets of characters
import string
import random

from sqlalchemy import inspect
from tools.url_shortner import shorten_url_pyshorteners

# To Store the short URL and their associated URLS
url_map={}
nanourl=Flask(__name__)
#Configuring the database
nanourl.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
nanourl.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Creating the database instance
db=SQLAlchemy(nanourl)

class Urlshortenr(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    original_url=db.Column(db.String(500),nullable=False)
    short_url=db.Column(db.String(10),unique=True,nullable=True)
    created_at=db.Column(db.DateTime,nullable=False,server_default=db.func.now())
 
 
 
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encode_62(num):
    if num==0:
        return BASE62[0]
    arr=[]
    while num:
        rem = num%62
        arr.append(BASE62[rem])
        num//=62
    arr.reverse()
    return "".join(arr)   
#Save the longurl to Database
@nanourl.route("/shorten",methods=["POST"])
def url_shortener():
    long_url=request.form.get("url_sumi").strip()
    if not long_url or not long_url.startswith(("http://","https://")) or " " in long_url:
        return "Invalid Url"
    existing_url=Urlshortenr.query.filter_by(original_url=long_url).first()
    if existing_url:
        return f"{existing_url.short_url}"
    submit_original_url=Urlshortenr(original_url=long_url)
    db.session.add(submit_original_url)
    db.session.flush()
    offset=100000
    short_code=encode_62(submit_original_url.id+offset)
    submit_original_url.short_url=short_code
    db.session.commit()
    display_url=f"http://nanourl.com/{short_code}"
    return f"{display_url} is saved"

def decode_62(short_code):
    num=0
    for char in short_code:
        num=num*62+BASE62.index(char)
    return num

    
@nanourl.route("/")
def index():
    return render_template("index.html")
    
# def home():
#     if request.method=="POST":uv
#         name=request.form.get("name")
#         user=User(name=name)
#         db.session.add(user)
#         db.session.commit()
#     return render_template("user.html")

# @nanourl.route("/c/users",methods=['GET'])
# def users():
#     all_users = User.query.all()
#     return render_template("user.html", all_users=all_users)

# class User(db.Model):
#     id =db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100))

#     def __repr__(self):
#         return f"id :{self.id}name:{self.name}"
    


 
# def generate_short_url():
#     characters = string.ascii_uppercase+string.ascii_lowercase
#     return "".join(random.choices(characters,k=6))
    
# @nanourl.route('/',methods=["GET","POST"])
# def index():
#     google_sh = shorten_url_pyshorteners("google.com")
#     shorten_url=None
#     if request.method=="POST":
#         shorten_url=generate_short_url()
#     return render_template("index.html",shorten_url=google_sh)

# Run the application
if __name__=='__main__':
    with nanourl.app_context():
        db.create_all()
    #     inspector = inspect(db.engine)
    #     users=User.query.all()
    # print(inspector.get_table_names())
    # print(users)
    nanourl.run(debug=True)

