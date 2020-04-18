from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Dormitory

dormitoryBlue = Blueprint('dormitoryBlue', __name__)


@dormitoryBlue.route('/Dormitory/info', methods=['POST', 'GET'])
def dormitoryInfo():
    # TODO check if has existed => or register dormitory info
    if request.method == 'GET':
        item = session.get('user')
        print(item)
        dormitory = Dormitory.query.filter(Dormitory.dormitoryId == item.get('roomId')).first()
        return render_template('DormitorySystem/dormitoryInfo.html', dormitory=dormitory)
    return None


@dormitoryBlue.route('/Dormitory/payment', methods=['POST', 'GET'])
def dormitoryPayment():
    dormitory = Dormitory.query.filter(Dormitory.dormitoryId == session.get('user').get('roomId')).first()
    print(request.method)
    if request.method == 'GET':
        return render_template('DormitorySystem/dormitoryPayment.html', dormitory=dormitory)
    else:
        if request.form.get('dormitoryPayment_remainLight') is not None:
            dormitory.remainLight = int(dormitory.remainLight) + int(request.form.get('dormitoryPayment_remainLight'))

        if request.form.get('dormitoryPayment_remainWater') is not None:
            dormitory.remainWater = int(dormitory.remainWater) + int(request.form.get('dormitoryPayment_remainWater'))

        db.session.add(dormitory)
        db.session.commit()

        return render_template('DormitorySystem/dormitoryPayment.html', dormitory=dormitory)


@dormitoryBlue.route('/Dormitory/mainPage')
def dormitoryCheck():
    return render_template('DormitorySystem/dormitoryMainPage.html')
