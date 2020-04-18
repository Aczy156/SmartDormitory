from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Log

logBlue = Blueprint('logBlue', __name__)


@logBlue.route('/Log/historyInfo', methods=['POST', 'GET'])
def logHistoryInfo():
    logList = Log.query.filter(Log.isIn == 'True').all()
    return render_template('/LogSystem/logHistoryInfo.html', logList=logList)


@logBlue.route('/Log/selectHistory', methods=['POST', 'GET'])
def dormitoryPayment():
    return None
