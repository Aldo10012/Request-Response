
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greating to the User."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """Shows animal."""
    return 'Penguins are cute!'

@app.route('/dogs')
def dogs():
    """Shows my favorit animal."""
    return 'Dogs are the coolest! They are cute, playful, and loyal friends. '

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_desert(users_dessert):
    """ Display a message to the user based on what dessert they like. """
    return f'How did I know you liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """ Display a madlib """
    return f'Petter was camping in the woods. There, he say a {noun} that was pritty {adjective}.'

@app.route('/multiply/<num1>/<num2>')
def multiply_2_nums(num1,num2):
    """Displays teh product of 2 numbers"""
    return f'{num1} times {num2} is {int(num1) * int(num2) }'


if __name__ == '__main__':
    app.run(debug=True)