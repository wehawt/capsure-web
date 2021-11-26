from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/", methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('homepage'))
    return render_template("homepage.html")

@sample.route('/signin',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('signin'))
    return render_template("signin.html")

@sample.route('/welcome',methods=['POST','GET'])
def welcome():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('welcome'))
    return render_template("welcome.html")



if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080 , debug=True)
