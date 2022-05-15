from flask import Flask, jsonify,render_template
from app.election_scraper import scrape_election
import json

app = Flask(__name__)

@app.route("/")
def index():
    result = scrape_election()
    return render_template('index.html', data=result)