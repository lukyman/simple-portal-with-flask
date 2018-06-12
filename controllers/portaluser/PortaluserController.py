from app import app, render_template, request, redirect, url_for, db
from models.portaluser import PortalUser
from datetime import datetime
from decorators.auth_docratory import authorize
import bcrypt

index_template = 'portaluser/index.html'
default_password = '1234'


@app.route('/portaluser', methods=['GET'])
@authorize
def get_index_view():
    portalusers = PortalUser.query.all()
    return render_template(index_template, portalusers=portalusers)


@app.route('/portaluser', methods=['POST'])
@authorize
def create_portaluser():
    
    fullname = request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    active = True
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    
    isAvailable = PortalUser.query.filter(
        (username==username)| (email==email)).first()

    if isAvailable:
        return redirect(url_for('get_index_view'))

    hashed_password = bcrypt.hashpw(default_password, bcrypt.gensalt())

    portaluser = PortalUser(
        fullname,
        username,
        email,
        hashed_password,
        active,
        created_at,
        updated_at
    )
    print portaluser.fullname

    db.session.add(portaluser)
    db.session.commit()

    return redirect(url_for('get_index_view'))
