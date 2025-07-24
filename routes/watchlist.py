# routes/watchlist.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.watchlist import get_watchlist, add_to_watchlist, remove_from_watchlist

watchlist_bp = Blueprint('watchlist', __name__, url_prefix='/watchlist')

@watchlist_bp.route('/')
def index():
    return render_template('watchlist.html', watchlist=get_watchlist())

@watchlist_bp.route('/add', methods=['POST'])
def add():
    name = request.form.get("name", "").strip()
    if name:
        if add_to_watchlist(name):
            flash(f"Added {name} to watchlist", "success")
        else:
            flash(f"{name} is already in the watchlist", "info")
    return redirect(url_for("watchlist.index"))

@watchlist_bp.route('/remove', methods=['POST'])
def remove():
    name = request.form.get("name", "").strip()
    if name:
        if remove_from_watchlist(name):
            flash(f"Removed {name} from watchlist", "success")
        else:
            flash(f"{name} was not in the watchlist", "info")
    return redirect(url_for("watchlist.index"))