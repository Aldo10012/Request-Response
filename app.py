
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greating to the User."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def homepage_penguins():
    """Shows my favorit animal."""
    return 'Penguins are cute!'

@app.route('/dogs')
def homepage_dogs():
    """Shows my favorit animal."""
    return 'Dogs are the coolest! They are cute, playful, and loyal friends. '



if __name__ == '__main__':
    app.run(debug=True)