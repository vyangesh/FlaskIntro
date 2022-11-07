from flask import Flask

#imported modules

app = Flask(__name__)#created Flask object. This will tell Flask where to look for resources.


@app.route('/')
#This will tell Flask what URL to use to trigger the function.


#The function below returns HTML by default. So the string in return statement will reder as HTML
def index():
    return "<h1>Hello, world</h>"

#the below will be used for debuggging
if __name__=="__main__":
    app.run(debug=True)