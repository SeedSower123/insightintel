import os
from flask import Flask, redirect

# Import blueprints
from routes.dashboard import dashboard_bp
from routes.signals import signals_bp
from routes.about import about_bp
from routes.watchlist import watchlist_bp
from routes.sec import sec_bp

app = Flask(__name__)

# Security: Require SECRET_KEY env variable for session management, etc.
secret_key = os.environ.get("SECRET_KEY")
if not secret_key:
    raise RuntimeError("SECRET_KEY environment variable must be set for security.")
app.config['SECRET_KEY'] = secret_key

# Register blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(signals_bp)
app.register_blueprint(about_bp)
app.register_blueprint(watchlist_bp)
app.register_blueprint(sec_bp)

# Redirect root URL to dashboard
@app.route('/')
def index():
    return redirect('/dashboard/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Enable debug=True for development; turn off in production
    app.run(host='0.0.0.0', port=port, debug=True)