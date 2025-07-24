from flask import Blueprint, render_template, request, redirect, url_for, session

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def index():
    watchlist = session.get('watchlist', [])
    return render_template('dashboard.html', watchlist=watchlist)

@dashboard_bp.route('/add/<company>')
def add_to_watchlist(company):
    watchlist = session.get('watchlist', [])
    if company not in watchlist:
        watchlist.append(company)
    session['watchlist'] = watchlist
    return redirect(url_for('dashboard.index'))