from flask import Blueprint, render_template, jsonify
from utils.sec_fetcher import fetch_recent_filings

sec_bp = Blueprint('sec', __name__, url_prefix='/sec')

@sec_bp.route('/fetch')
def fetch():
    filings = fetch_recent_filings()
    return render_template('sec.html', filings=filings)

@sec_bp.route('/fetch/data')
def fetch_data():
    filings = fetch_recent_filings()
    return jsonify(filings=filings)