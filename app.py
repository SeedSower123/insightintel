import os
from flask import Flask, redirect, session
from flask_session import Session

from routes.dashboard import dashboard_bp
from routes.signals import signals_bp
from routes.about import about_bp

app = Flask(__name__, static_folder='static', template_folder='templates')
secret_key = os.environ.get('SECRET_KEY')
if not secret_key:
    raise RuntimeError("SECRET_KEY environment variable must be set for security.")
app.secret_key = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.register_blueprint(dashboard_bp)
app.register_blueprint(signals_bp)
app.register_blueprint(about_bp)

@app.route('/')
def index():
    return redirect('/dashboard')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)