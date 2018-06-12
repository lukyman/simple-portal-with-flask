from app import app, render_template, request, redirect, url_for, db
from models.merchant import Merchant
from models.MerchantCode import MerchantCode
from datetime import datetime
from decorators.auth_docratory import authorize
from util.random_string_generator import RandomString

index_template = 'merchant/index.html'


@app.route('/merchant', methods=['GET'])
@authorize
def index_merchant():
    all_merchants = Merchant.query.all()
    return render_template(index_template, merchants=all_merchants)


@app.route('/merchant', methods=['POST'])
@authorize
def add_merchant():

    codeis_unique = False
    code = ''
    random_string_generator = RandomString()
    while codeis_unique is False:
        code = random_string_generator.generate(8)
        codeis_unique = Merchant.query.filter_by(code=code).first()
        if codeis_unique is None:
            codeis_unique = True
    
    
    print request.form
    business_name = request.form['business_name']
    registration_number = request.form['business_regno']
    date_of_reg = request.form['date_of_reg']
    email = request.form['email']
    physical_address = request.form['physical_address']
    box_number = request.form['box_number']

    new_merchant = Merchant(
        business_name,
        registration_number,
        date_of_reg,
        email,
        physical_address,
        box_number,
        code = code
    )
    db.session.add(new_merchant)
    db.session.commit()

    # save used code to db 
    merchant_code = MerchantCode(
        code,
        datetime.utcnow(),
        datetime.utcnow()
    )
    db.session.add(merchant_code)
    db.session.commit()
    
    return  redirect(url_for('index_merchant'))
