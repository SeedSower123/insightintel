import os
from flask import Flask, redirect, session
from flask_session import Session
app = Flask(__name__)

# Import Blueprints
from routes.watchlist import watchlist_bp

app.register_blueprint(watchlist_bp)
from routes.dashboard import dashboard_bp
from routes.signals import signals_bp
from routes.about import about_bp

app = Flask(__name__, static_folder='static', template_folder='templates')

# ✅ Set secret key for session security, with fallback for local development
app.secret_key = os.environ.get('SECRET_KEY', 'dev')  # Use 'dev' as default for local

# ✅ Configure session storage
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# ✅ Register blueprints (modular route handling)
app.register_blueprint(dashboard_bp)
app.register_blueprint(signals_bp)
app.register_blueprint(about_bp)

# ✅ Redirect root to dashboard
@app.route('/')
def index():
    return redirect('/dashboard')

# ✅ Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
    from routes.sec import sec_bp
app.register_blueprint(sec_bp)