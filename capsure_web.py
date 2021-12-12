from flask import json, url_for
from flask import redirect
from flask import jsonify
from flask import request
from flask import Flask
from flask import render_template
import sqlite3 as sql
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from sqlalchemy import text


cap_app = Flask(__name__)
cap_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
cap_app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(cap_app)
ma = Marshmallow(cap_app)


class User(db.Model):
    tablename = "user"
    user_id = db.Column(db.String(50), primary_key=True)
    user_fname = db.Column(db.String(50))
    user_lname = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50))
    user_number = db.Column(db.String(50))
    user_address = db.Column(db.String(50))
    user_city = db.Column(db.String(50))
    user_zipcode = db.Column(db.String(50))

    def __init__(self, user_id, user_fname, user_lname, user_email, user_password, user_number, user_address, user_city, user_zipcode):
        self.user_id = user_id
        self.user_fname = user_fname
        self.user_lname = user_lname
        self.user_email = user_email
        self.user_password = user_password
        self.user_number = user_number
        self.user_address = user_address
        self.user_city = user_city
        self.user_zipcode = user_zipcode


class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_fname" , "user_lname", "user_email", "user_password", "user_number", "user_address", "user_city", "user_zipcode")

user_schema = UserSchema()
users_schema = UserSchema(many=True)




@cap_app.route('/regis', methods=['POST'])
def regis():  
    if request.method == 'POST':
        json_data = request.get_json()
        user_id = datetime.now().strftime("%m%d%H%M%S")
        user_fname = json_data[0]["fname_signup"]
        user_lname = json_data[0]["lname_signup"]
        user_email = json_data[0]['email_signup']
        user_password = json_data[0]['password_signup']
        user_number = json_data[0]['number_signup']
        user_address = json_data[0]['address_signup']
        user_city = json_data[0]['city_signup']
        user_zipcode = json_data[0]['zipcode_signup']

        new_user = User(user_id, user_fname, user_lname, user_email, user_password, user_number, user_address, user_city, user_zipcode)
        db.session.add(new_user)
        db.session.commit()

        message = {"message":"Account Created Successfuly"}
        return jsonify(message)

#------------------Render-----------------------------
@cap_app.route('/createdAcc', methods=['GET', 'POST'])
def createdAcc():
    return render_template('signin.html')
    

@cap_app.route('/login', methods=['GET'])
def login():  
    return render_template("signin.html")

#----------------------------------------------------

@cap_app.route('/validate', methods=['POST'])
def validate():
    if request.method == 'POST':

        json_data = request.get_json()
        email = json_data[0]["email"]
        password = json_data[0]["password"]
        user = User.query.filter_by(user_email=email).first()
        user = user_schema.dump(user)
        

        if(len(user)>0):
            if (user['user_password'] == password):
                message = {"message":"Successfuly logged in"}
            else:
                user = None
                message = {"message":"Incorrect Credentials"}

        else:
            user = None
            message = {"message":"Incorrect Credentials"}

    return jsonify(message)

@cap_app.route("/", methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('homepage'))
    return render_template("homepage.html")

@cap_app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('signin'))
    return render_template("signin.html")

@cap_app.route('/welcome',methods=['POST','GET'])
def welcome():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('welcome'))
    return render_template("welcome.html")

@cap_app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('signup'))
    return render_template("signup.html")


@cap_app.route('/about',methods=['POST','GET'])
def about():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('about'))
    return render_template("about.html")




if __name__ == "__main__":
    db.create_all()
    cap_app.run(host="0.0.0.0", port=8080 , debug=True)



