from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#imported modules

app = Flask(__name__)#created Flask object. This will tell Flask where to look for resources.

#below we will create a DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'#here we use /// which means rel path. //// means absolute path
db = SQLAlchemy(app)#created obj for class SQLAlchemy and passed the app obj of class Flask


#now we create a class by passing the arg db.Model which is a function inside class SQLAlchemy.
#this class will create the sturucture of our table
class Todo(db.Model):
    #the code below this...
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #...Until here will be fired automatically. We do not have to invoke it manually or write a code to invoke this part

    #this function will return the id of the new element created. This will be in string format.
    def __repr__(self):
        return '<Task %r>' %self.id

########################################33
#Now, to create a database using Flask we will use the above code.
#Since we need to do it only once we will do it in the terminal.
#In the terminal, we will make use of the above code by importing db object.
#We need to do all this inside the env and under the directory we want our DB file to be in. In this case we will do it in the current dir
#This will be inside interactive python
#>from app import db #app here is the app.py file and not the variables used inside it
#>db.create_all()
#now you should have a file (test.db) under the directory under the directory you ran it from
#
####################################################################



@app.route('/', methods=['POST','GET'])
#This will tell Flask what URL to use to trigger the function.
#Added methods that we can use. By default we use only GET, but now we can even post on the webpage



#The function below returns the template passed through it. It does not require the entire path to the file index.html
#because of the folder name given to the "templates", it knows to look into that folder.
def index():
    return render_template('index.html')

#the below will be used for debuggging
if __name__=="__main__":
    app.run(debug=True)