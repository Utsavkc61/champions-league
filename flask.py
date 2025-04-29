''' for when database is ready
from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages!

# Assume you have a Player model and database setup
from your_database_models import Player, db

@app.route('/add-player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        jersey_number = request.form['jersey_number']
        team = request.form['team']
        dob = request.form['dob']
        country = request.form['country']

        # Save the player to the database
        new_player = Player(name=name, jersey_number=jersey_number, team=team, date_of_birth=dob, country=country)
        db.session.add(new_player)
        db.session.commit()

        # Flash a success message!
        flash('Player added successfully!', 'success')

        return redirect(url_for('players'))  # redirect back to the Players page

    return render_template('add-player.html')

# Assuming you have this to display all players
@app.route('/players')
def players():
    all_players = Player.query.all()
    return render_template('players.html', players=all_players)
'''

from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages!

@app.route('/add-player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        # name = request.form['name']
        # jersey_number = request.form['jersey_number']
        # team = request.form['team']
        # dob = request.form['dob']
        # country = request.form['country']

        # Simulate "saving" the player (no database yet!)
        flash('Player added successfully!', 'success')

        return redirect(url_for('players'))  # Redirect to players page

    return render_template('add-player.html')

@app.route('/players')
def players():
    
    #pass a fake player dicitonary for now

    player = {
        'name': 'Lionel Messi',
        'country': 'Argentina',
        'team': {'name': 'Inter Miami'},
        'position': 'Forward',
        'date_of_birth': '1987-06-24',
        'jersey_number': 10
    }
    return render_template('players.html', player=player) 
