# -*- coding: UTF-8 -*-
from App.configurations.ext import db


# User System
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    number = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    roomId = db.Column(db.Integer)
    roomname = db.Column(db.String(100))
    department = db.Column(db.String(100))
    myclass = db.Column(db.String(100))
    roommate1 = db.Column(db.String(100))
    roommate2 = db.Column(db.String(100))
    roommate3 = db.Column(db.String(100))

    introduction = db.Column(db.String(100))
    userPicture = db.Column(db.String(100))


# Dormintory System
class Dormitory(db.Model):
    dormitoryId = db.Column(db.Integer, primary_key=True)
    dormitoryName = db.Column(db.String(100))
    dormitoryNumber = db.Column(db.String(100))
    dormitoryManager = db.Column(db.String(100))

    member1 = db.Column(db.String(100))
    member2 = db.Column(db.String(100))
    member3 = db.Column(db.String(100))
    member4 = db.Column(db.String(100))

    innerTemperature = db.Column(db.String(100))
    innerHumidity = db.Column(db.String(100))

    remainWater = db.Column(db.Integer)
    remainLight = db.Column(db.Integer)


# Camera System
class Log(db.Model):
    logId = db.Column(db.Integer, primary_key=True)
    logTime = db.Column(db.String(100))
    logPerson = db.Column(db.String(100))
    logSource = db.Column(db.String(200))
    isIn = db.Column(db.String(50))
