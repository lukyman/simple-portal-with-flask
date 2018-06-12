from app import app, db, request,make_response,render_template, redirect, url_for
import bcrypt
from models.portaluser import PortalUser
import json

@app.route('/auth/login', methods=['GET'])
def get_login():
    return render_template('/auth/login.html')

@app.route('/auth/login', methods=['POST'])
def make_login():
    username = request.form['username']
    password = request.form['password']
    
    if not username or not password:
        return redirect('/auth/login')

    user = PortalUser.query.filter_by(username=username).first()
    print user.password
    if user:
        password_isvalid = bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8'))
        print password_isvalid
        if password_isvalid:
            
            resp = make_response(redirect('/'))
            resp.set_cookie('user', user.username)
            return resp
        else:
           return redirect('/auth/login')
    else:
        return redirect('/auth/login')

