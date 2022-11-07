from flask import Flask, render_template, url_for

#imported modules

app = Flask(__name__)#created Flask object. This will tell Flask where to look for resources.


@app.route('/')
#This will tell Flask what URL to use to trigger the function.


#The function below returns the template passed through it. It does not require the entire path to the file index.html
#because of the folder name given to the "templates", it knows to look into that folder.
def index():
    return render_template('index.html')

#the below will be used for debuggging
if __name__=="__main__":
    app.run(debug=True)