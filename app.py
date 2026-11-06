# Import Flask so the application can use the Flask web framework.
from flask import Flask

# Create the Flask application object for this project.
app = Flask(__name__)


# Connect the website's root URL to the home function.
@app.route("/")
# Define the function that responds to requests for the home page.
def home():
    # Send the cafe's welcome message back to the browser.
    return "Welcome to Cafe Gharti"


# Connect the /about URL to the about function.
@app.route("/about")
# Define the function that responds to requests for the about page.
def about():
    # Send one sentence describing the cafe back to the browser.
    return "Cafe Gharti is a welcoming cafe serving delicious food and drinks."