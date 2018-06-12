from app import app, render_template
from decorators.auth_docratory import authorize
@app.route('/')
@authorize
def index():
    return render_template('shared/layout.html')