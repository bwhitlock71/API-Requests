from flask import Flask, render_template, request
from secrets_1 import key


API_BASE_URL='https://www.mapquestapi.com/geocoding/v1/address'

# API key is in a different python file.

app = Flask(__name__)

@app.route('/')
def show_address_form():
    return render_template("address_form.html")