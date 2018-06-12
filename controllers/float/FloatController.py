from app import db, redirect, render_template, request, app, make_response
from models.merchant import Merchant
from models.float import FloatUpdate, FloatBalance, FloatConsumption, FloatUpdateSchema, FloatBalanceSchema
from decorators.auth_docratory import authorize
from flask import jsonify
from datetime import datetime


@app.route('/float', methods=['GET'])
@authorize
def indexview():
    merchants = Merchant.query.all()
    return render_template('float/index.html', merchants=merchants)


@app.route('/float/balance/merchant/<merchantid>')
@authorize
def get_merchant_balance(merchantid):
    float_balance_schema = FloatBalanceSchema()

    balance = FloatBalance.query.filter_by(merchant_id=merchantid).first()

    return jsonify(float_balance_schema.dump(balance))


@app.route('/float/updates/merchant/<merchantid>')
@authorize
def get_update_history(merchantid):

    ### Initialize Schema to convert Model class to Dict
    float_update_schema = FloatUpdateSchema(many=True)

    updates = FloatUpdate.query.filter_by(merchant_id=merchantid).all()
    updates_dict = float_update_schema.dump(updates)
    return jsonify(updates_dict)


@app.route('/float/<merchantid>', methods=['POST'])
@authorize
def updatefloat(merchantid):
    reqbody = request.get_json()
    amount = int(reqbody['amount'])
    merchantid = int(merchantid)

    new_float = FloatUpdate(
        merchantid, amount, datetime.utcnow(), datetime.utcnow())

    db.session.add(new_float)
    db.session.commit()

    if new_float.id > 0:
        merchant_balance = FloatBalance.query.filter_by(
            merchant_id=merchantid).first()
        if merchant_balance is None:
            new_balance = FloatBalance(
                merchantid, amount, datetime.utcnow(), datetime.utcnow())
            db.session.add(new_balance)
            db.session.commit()

            ### Get newly updated balance from db
            merchant_balance_updated = FloatBalance.query.filter_by(
                merchant_id=merchantid).first()

            ### return as json
            return jsonify(id=merchant_balance_updated.id,
                           merchantid=merchant_balance_updated.merchant_id,
                           amount=merchant_balance_updated.amount)
        else:
            merchant_balance.amount += amount
            merchant_balance.updated_at = datetime.utcnow()
            db.session.commit()

            ### Get newly updated balance from db
            merchant_balance_updated = FloatBalance.query.filter_by(
                merchant_id=merchantid).first()

            return jsonify(id=merchant_balance_updated.id,
                           merchantid=merchant_balance_updated.merchant_id,
                           amount=merchant_balance_updated.amount)
    else:
        return jsonify({})


@app.route('/float/check-availability', methods=['GET'])
def chech_float_availability():

    merchant_code = request.args.get('merchant_code')
    amount = float(request.args.get('amount'))
    merchant = Merchant.query.filter_by(code=merchant_code).first()
    if merchant:
        float_balance = FloatBalance.query.filter_by(
            merchant_id=merchant.id).first()
        if float_balance.amount > 0:
            if float_balance.amount >= amount:
                resp = make_response(jsonify(
                    message="Float available.",
                    status=True,
                ), 200)
                return resp
            else:
                topup = amount - float_balance.amount
                resp = make_response(jsonify(
                    message="Float not sufficient. Top up Ksh " +
                        str(topup)+" or more.",
                    status=False,
                ), 400)
                return resp
        else:
            topup = float_balance.amount - amount
            resp = make_response(jsonify(
                message="Float not sufficient. Top up Ksh " +
                    str(topup)+" or more.",
                status=False,
            ), 400)
            return resp
    else:
        resp = make_response(jsonify(
            message="Unauthorized merchant.",
            error=True
        ), 401)
        return resp


@app.route('/float/bill')
def charge_merchant():
    merchant_code = request.args.get('merchant_code')
    amount = float(request.args.get('amount'))
    merchant = Merchant.query.filter_by(code=merchant_code).first()
    
    if merchant:
        float_balance = FloatBalance.query.filter_by(merchant_id=merchant.id).first()
        if float_balance.amount > 0:
            if float_balance.amount >= amount:
                
                balance = float_balance.amount - amount
                float_balance.amount = balance

                # update the locked balance
                # code missing....

                resp = make_response(jsonify(
                    message="Float available.",
                    status=True,
                ), 200)
                return resp
            else:
                topup = amount - float_balance.amount
                resp = make_response(jsonify(
                    message="Float not sufficient. Top up Ksh "+str(topup)+" or more.",
                    status=False,
                ), 400)
                return resp
        else:
            topup = float_balance.amount - amount
            resp = make_response(jsonify(
                message="Float not sufficient. Top up Ksh "+ str(topup)+" or more.",
                status=False,
            ), 400)
            return resp
    else:
        resp = make_response(jsonify(
            message="Unauthorized merchant.",
            error=True
        ), 401)
        return resp
