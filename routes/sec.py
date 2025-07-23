from flask import Blueprint, jsonify
from utils.sec_fetcher import fetch_recent_filings

sec_bp = Blueprint('sec', __name__, url_prefix='/sec')

@sec_bp.route('/fetch')
def fetch_sec_data():
    data = fetch_recent_filings()
    return jsonify({"results": data})