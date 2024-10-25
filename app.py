# imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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

@app.route('/trainer', methods=['GET', 'POST'])
def trainer():
    return render_template('trainer.html')

def calculate_chips(amount):
    purple_chips = amount // 500
    amount = amount % 500
    black_chips = amount // 100
    amount = amount % 100
    green_chips = amount // 25
    amount = amount % 25
    red_chips = amount // 5
    amount = amount % 5
    white_chips = amount

    return int(white_chips), int(red_chips), int(green_chips), int(black_chips), int(purple_chips)

@app.route('/calculate_chips', methods=['POST'])
def calculate_chips_route():
    data = request.get_json()
    amount = data.get('amount', 0) 

    white, red, green, black, purple = calculate_chips(amount)

    return jsonify({
        'white_chips': white,
        'red_chips' : red,
        'green_chips' : green,
        'black_chips' : black,
        'purple_chips' : purple
    })


if __name__ == '__main__':
    app.run(debug=True)
