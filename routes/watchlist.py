from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.watchlist import get_watchlist, add_to_watchlist, remove_from_watchlist

watchlist_bp = Blueprint('watchlist', __name__, url_prefix='/watchlist')

@watchlist_bp.route('/', methods=['GET'])
def index():
    watchlist = get_watchlist()
    return render_template('watchlist.html', watchlist=watchlist)

@watchlist_bp.route('/add', methods=['POST'])
def add():
    name = request.form.get('name', '').strip()
    if name:
        if add_to_watchlist(name):
            flash(f'Added "{name}" to watchlist.', 'success')
        else:
            flash(f'"{name}" is already in watchlist.', 'info')
    else:
        flash('Name cannot be empty.', 'error')
    return redirect(url_for('watchlist.index'))

@watchlist_bp.route('/remove', methods=['POST'])
def remove():
    name = request.form.get('name', '').strip()
    if name:
        if remove_from_watchlist(name):
            flash(f'Removed "{name}" from watchlist.', 'success')
        else:
            flash(f'"{name}" not found in watchlist.', 'info')
    else:
        flash('Name cannot be empty.', 'error')
    return redirect(url_for('watchlist.index'))