import os
from random import shuffle
from flask import Flask , redirect, url_for, render_template,request,flash
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def making_buttonimgs():
    listt =  os.listdir('static/')
    shuffle(listt)
    return render_template("index.html", imgs_list =listt )
  
    

if __name__ == "__main__":
    app.run(debug=True)