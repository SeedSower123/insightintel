# routes/signals.py

from flask import Blueprint, render_template, jsonify
from utils.sec_fetcher import get_all_recent_signals

signals_bp = Blueprint('signals', __name__, url_prefix='/signals')

@signals_bp.route('/')
def index():
    signals = get_all_recent_signals()
    return render_template('signals.html', signals=signals)

@signals_bp.route('/data')
def data():
    signals = get_all_recent_signals()
    return jsonify(signals=signals)