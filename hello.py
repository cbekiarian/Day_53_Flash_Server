from flask import Flask

app = Flask(__name__)

print(__name__)

class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in =False

def authenticator_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper



@app.route("/")
@authenticator_decorator
def hello_world():
    new_user = User("Angela")
    new_user.is_logged_in = True
    return f"Hello, {new_user.name}! "

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/username/<name>")
def name (name):
    return f"hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)