# imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from bs4 import BeautifulSoup

# Setting up flask and app
app = Flask(__name__)
app.secret_key = 'blackjack.io'

# Create a new client and connect to the server
uri = "mongodb+srv://avadlamani:Breakingbad1928!@cluster0.2ohfz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Databases
db = client['CardCountingProject']
users_collection = db['User info']
training_collection = db['Training data']

# chip dict
chip_dict = {"white": 1, "red": 5, "green": 25, "black": 100, "purple": 500}

# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

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
                session['username'] = username
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
    session.pop('_flashes', None)
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

def calculate_chips(amount, buyin_initial):
    username = session.get('username')
    training_collection.insert_one({
    'username': username,
    'bankroll': amount,
    'buyin': buyin_initial,
    'Timestamp': datetime.now().strftime("%B %d, %Y @ %I:%M:%S %p")
    })

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

    white, red, green, black, purple = calculate_chips(amount, buyin_initial=amount)

    return jsonify({
        'white_chips': white,
        'red_chips' : red,
        'green_chips' : green,
        'black_chips' : black,
        'purple_chips' : purple
    })

# Helper function to retrieve the user's current bankroll
def get_current_bankroll(username):
    # Retrieve the latest bankroll entry for the user
    user_data = training_collection.find({"username": username}).sort("_id", -1).limit(1)
    return user_data[0].get('bankroll', 0)

# Helper function to retrieve the user's current buyin
def get_current_buyin(username):
    user_data = training_collection.find({"username": username}).sort("_id", -1).limit(1)
    return user_data[0].get('buyin', 0)

# New route to handle bankroll updates
@app.route('/update_bankroll', methods=['POST'])
def update_bankroll():
    data = request.get_json()
    additional_amount = data.get('additional_amount', 0)
    username = session.get('username')

    # Retrieve the current bankroll
    current_bankroll = get_current_bankroll(username)
    
    # Calculate the new bankroll
    new_bankroll = current_bankroll + additional_amount

    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )
    
    # Update the user's bankroll and buyin in MongoDB
    training_collection.update_one(
            {"_id": most_recent_entry['_id']},
            {"$set": {"bankroll": new_bankroll, "buyin": get_current_buyin(username) + additional_amount}}
    )

    white, red, green, black, purple = calculate_chips(new_bankroll, 0)

    # eliminate redundancies
    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )

    result = training_collection.delete_one({"_id": most_recent_entry['_id']})

    # Return the new bankroll and chip counts
    return jsonify({
        "new_bankroll": new_bankroll,
        "white_chips": white,
        "red_chips": red,
        "green_chips": green,
        "black_chips": black,
        "purple_chips": purple
    })

# Chip pressed route
@app.route('/chip_pressed', methods=['POST'])
def chip_pressed():
    username = session.get('username')
    data = request.get_json()
    chip_type = data.get('button_type', 0)
    # Retrieve the current bankroll
    current_bankroll = get_current_bankroll(username)

    change_in_bankroll = chip_dict[chip_type]

    # return chip values for updating
    white = int(data.get('white'))
    red = int(data.get('red'))
    green = int(data.get('green'))
    black = int(data.get('black'))
    purple = int(data.get('purple'))

    # eliminate reduncancies
    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )
    _ = training_collection.delete_one({"_id": most_recent_entry['_id']})

    # checking if button pressed, but 0 chips are there
    if (chip_type == "white" and white == 0) or (chip_type == "red" and red == 0) or (chip_type == "green" and green == 0) or (chip_type == "black" and black == 0) or (chip_type == "purple" and purple == 0):
        return jsonify({
            "new_bankroll": current_bankroll,
            "white_chips": white,
            "red_chips": red,
            "green_chips": green,
            "black_chips": black,
            "purple_chips": purple
        })

    # now update bankroll in database and on screen
    # also update chip counts

    new_bankroll = current_bankroll - change_in_bankroll
    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )

    training_collection.update_one(
            {"_id": most_recent_entry['_id']},
            {"$set": {"bankroll": new_bankroll}}
    )

    # update chip counts
    if chip_type == "white":
        white -= 1
    elif chip_type == "red":
        red -= 1
    elif chip_type == "green":
        green -= 1
    elif chip_type == "black":
        black -= 1
    elif chip_type == "purple":
        purple -= 1
    
    return jsonify({
        "new_bankroll": new_bankroll,
        "white_chips": white,
        "red_chips": red,
        "green_chips": green,
        "black_chips": black,
        "purple_chips": purple
    })

# return current bankroll
@app.route('/current_bankroll', methods=['GET'])
def current_bankroll():
    username = session.get('username')
    if not username:
        return jsonify({'bankroll': 0})
    
    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )
    return jsonify({'bankroll': most_recent_entry['bankroll']}) if most_recent_entry else jsonify({'bankroll': 0})

@app.route('/current_buyin', methods=['GET'])
def current_buyin():
    username = session.get('username')
    if not username:
        return jsonify({'buyin': 0})
    
    most_recent_entry = training_collection.find_one(
        {"username": username},
        sort=[('_id', -1)]  # Sort by _id to get the most recent entry
    )
    return jsonify({'buyin': most_recent_entry['buyin']}) if most_recent_entry else jsonify({'buyin': 0})

@app.route('/past_data')
def pastData():
    username = session.get('username')
    data = training_collection.find({"username": username}, {"_id": 0, "username": 0})

    return render_template('pastData.html', data=list(data.sort("Timestamp", -1)), username=username)

if __name__ == '__main__':
    app.run(debug=True)
