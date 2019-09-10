from flask import Flask

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behavior
# connect url to the return value in the function
@app.route('/')
def index():
    return 'This is main page'  # what user sees

# pass variable in
# if need to pass integer variable, add <int:whatever_the_name>
@app.route('/user_login/<username>')
def user_login(username):
    return "<h2>Your username is %s</h2>" % username


if __name__ == '__main__':
    app.run()
