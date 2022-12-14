from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

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
#Added methods that we can use. By default we use only GET, but now we can even POST on the webpage



#The function below returns the template passed through it. It does not require the entire path to the file index.html
#because of the folder name given to the "templates", it knows to look into that folder.
#if we are POSTing then then we will show insert contents to test.db and if we are not then we retrive the page with the test.db tasks
def index():
    if request.method == 'POST':
        task_content = request.form['content']#getting the contents from the webpage
        new_task = Todo(content=task_content)#created an object under class Todo by passing the content(a column in the DB)

        try:
            db.session.add(new_task)#inserting a new row to the existing DB test.db
            db.session.commit()#saving changes in the test.db
            return redirect('/')#redirected to the page
        except:
            return 'There was an error while adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()#This will return all the content from test.db and display it in order they were created
        return render_template('index.html', tasks=tasks)#here we set the "tasks" in the index.html to tasks that we created in the line above

#for deleteing we need to re-route it to /delete/id from test.db which is the primary key of the task
@app.route('/delete/<int:id>')

#below function will fetch the task id and delete it from test.db.
#If successfully deleted it will redirect to the home page
#else it will show an error
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue while deleting this task."

#Rerouting to update
@app.route('/update/<int:id>', methods=['POST','GET'])

#Below function will grab the task id and update it in test.db
#If successfully deleted it will redirect to the home page
#else it will show an error
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        try:
            task_to_update.content = request.form['content']
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating the task."
    else:
        return render_template('update.html', task=task_to_update)



#the below will be used for debuggging
if __name__=="__main__":
    app.run(debug=True)