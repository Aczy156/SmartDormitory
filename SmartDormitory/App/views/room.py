from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Room

roomblue = Blueprint('roomblue', __name__)


@roomblue.route('/DormitorySystem/dormitoryInfo', methods=['POST', 'GET'])
def dormitoryInfo():
    # TODO check if has existed => or register dormitory info
    if request.method == 'GET':
        item = session.get('user')
        print(item)
        dormitory = Room.query.filter(Room.dormitoryId == item.get('roomId')).first()
        return render_template('DormitorySystem/dormitoryInfo.html', dormitory=dormitory)
    return None


@roomblue.route('/DormitorySystem/dormitoryPayment', methods=['POST', 'GET'])
def roommoney():
    dormitory = Room.query.filter(Room.dormitoryId == session.get('user').get('roomId')).first()
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


@roomblue.route('/DormitorySystem/roomcheck')
def dormitoryCheck():
    return render_template('DormitorySystem/roomcheck.html')

