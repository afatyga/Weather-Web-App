from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def root():
    return render_template(
        'mainpage.html')

@app.route('/temp')
def temp():
    return render_template(
        'temptest.html')

if __name__ == '__main__':

    app.run()
