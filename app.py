# imports
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.server_api import ServerApi


# Setting up flask and app
app = Flask(__name__)
app.secret_key = 'blackjack.io'

# Create a new client and connect to the server
uri = "mongodb+srv://avadlamani:Breakingbad1928!@cluster0.2ohfz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Databases
db = client['CardCountingProject']
users_collection = db['User info']

@app.route('/trainer', methods=['GET', 'POST'])
def trainer():
    return render_template('trainer.html')

# login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # check if username exists
        existing_user = users_collection.find_one({"username": username})

        # when user exists
        if existing_user:
            correct_password = existing_user["password"]
            if password == correct_password:
                flash('Login Successful!')
                return redirect(url_for('trainer'))
            else:
                flash('Incorrect Username/Password.')
        else:
            flash('Incorrect Username/Password.')
        return redirect(url_for('login'))
    
    # render login html file
    return render_template('login.html')

# register user page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # checking if username already exists
        existing_user = users_collection.find_one({"username": username})

        # when user exists
        if existing_user:
            flash('Username already exists. Please pick another one.')
            return redirect(url_for('register'))
        
        # when user doesn't already exist, add user data to 
        else:
            new_user = {
                "username" : username,
                "password" : password
            }
            users_collection.insert_one(new_user)
            flash("Registration successful")
        
        # after registering redirect users to the login file
        return redirect(url_for('login'))
    
    # render register html file
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
