import string
import random
from flask import Flask, request, redirect

app = Flask(__name__)

url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))  

@app.route('/')
def index():
    return "Welcome to the URL shortener!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    return f": {request.host_url}{short_code}"

@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found!", 404

app.run()
