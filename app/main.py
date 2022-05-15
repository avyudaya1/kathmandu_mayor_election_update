from flask import Flask, jsonify,render_template
from app.election_scraper import scrape_election
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    result = scrape_election()
    print(result)
    return "hello"
    return render_template('index.html', data=result)