from flask import Blueprint, render_template, jsonify
signals_bp = Blueprint('signals', __name__, url_prefix='/signals')

@signals_bp.route('/')
def index():
    return render_template('signals.html')

@signals_bp.route('/data')
def data():
    return jsonify(signals=[])