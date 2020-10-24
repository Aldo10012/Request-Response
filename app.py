import random
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

# Stretch challenges
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word,n):
    str = ''
    for x in range(int(n)):
        str += word + " "
    """Displays word chosed printed x times"""
    return f'{str}'

@app.route('/reverse/<word>')
def reverse_a_string(word):
    str=''
    for letter in word:
        str = letter + str 
    """displays word choses printed backwards"""
    return f'{str}'

@app.route('/strangecaps/<word>')
def strange_caps(word):
    str = ''
    cap = False
    for letter in word:
        if cap:
            str += letter.upper()
            cap = False
        else:
            str += letter.lower()
            cap = True
    return(f"{str}")

@app.route('/dicegame')
def dice_game():
    diceroll = random.randint(1,6)
    if diceroll < 6:
        return  f'You rolled a {diceroll}, you lose!'
    else:
        return f'You rolled a {diceroll}, you win!'



if __name__ == '__main__':
    app.run(debug=True)