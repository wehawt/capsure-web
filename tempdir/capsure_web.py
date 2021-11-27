from flask import url_for
from flask import redirect
from flask import jsonify
from flask import request
from flask import Flask
from flask import request
from flask import render_template
import sqlite3 as sql
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from sqlalchemy import text


sample = Flask(__name__)
sample.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
sample.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(sample)
ma = Marshmallow(sample)


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




@sample.route('/createdAcc', methods=['GET', 'POST'])
def createdAcc():
    if request.method == 'POST':
        user_id = datetime.now().strftime("%m%d%H%M%S")
        user_fname = request.form["fname_signup"]
        user_lname = request.form["lname_signup"]
        user_email = request.form['email_signup']
        user_password = request.form['password_signup']
        user_number = request.form['number_signup']
        user_address = request.form['address_signup']
        user_city = request.form['city_signup']
        user_zipcode = request.form['zipcode_signup']

        new_user = User(user_id, user_fname, user_lname, user_email, user_password, user_number, user_address, user_city, user_zipcode)
        db.session.add(new_user)
        db.session.commit()

        return render_template('homepage.html')
    

@sample.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email_login"]
        password = request.form["password_login"]

        query = text("SELECT * FROM user where user_email=:email and user_password=:password")
        query = query.columns(User.user_id, User.user_fname, User.user_lname, User.user_email, User.user_password, User.user_number, User.user_address, User.user_city, User.user_zipcode)

        users = db.session.query(User).from_statement(query).params(email=email, password=password).all()
        user = users_schema.dump(users)


        if (user is None):
            user = None
            return render_template("signin.html")
        else:
            if(len(user)>0):
                if (user[0]['user_email'] == email and user[0]['user_password'] == password):
                    return redirect(url_for("welcome")) 
                else:
                    return render_template("signin.html")

    return render_template("signin.html")


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

@sample.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('signup'))
    return render_template("signup.html")



if __name__ == "__main__":
    db.create_all()
    sample.run(host="0.0.0.0", port=8080 , debug=True)
