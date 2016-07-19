from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

INSULTS = ["horrible", "ugly", "mean", "cruel", "evil", "terrible"]


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Home page</title>
      </head>
      <body>
        <h1>Welcome to home page!</h1>
        <a href='/hello'>Click here to go to hello </a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          <label>Awesome <input type="radio" name="compliment" value="Awesome"></label>
          <label>Amazing<input type="radio" name="compliment" value="Amazing"></label>
          <label>coolio<input type="radio" name="compliment" value="coolio"></label>
          <label>Beautiful<input type="radio" name="compliment" value="Beautiful"></label>
          <label>Smart<input type="radio" name="compliment" value="Smart"></label><br>
          <br>
          <input type="submit"> <br>
          <br>
          </form>


        <form action="/diss">
          <label>See how bad you are here!<br><input type="submit"><br></label>
          <br>
        </form>
       
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person", "Friend")
    compliment = request.args.get("compliment", "Cool")

    #compliment = choice(AWESOMENESS)
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
         
      </body>
    </html>
    """ % (player, compliment)
@app.route('/diss')
def greet_diss():

    player = request.args.get("person", "Friend")
    insult = choice(INSULTS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
