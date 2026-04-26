from flask import Flask,redirect
import base64
nanourl=Flask(__name__)
@nanourl.route('/')
def home():
    return "Hello nanoUrl" 
if __name__=='__main__':
    nanourl.run(debug=True)