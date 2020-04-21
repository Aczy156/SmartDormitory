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


@logBlue.route('/Log/specificLog', methods=['POST', 'GET'])
def specificLog():
    print('is apply for getspecific log')
    print(request.args)
    logId = request.args['logId']
    print(logId)
    # logId = request.GET.get
    return render_template('/LogSystem/retrievalSpecificLog.html', logId=logId)


@logBlue.route('/Log/returnLogList', methods=['POST', 'GET'])
def returnLogList():
    logList = Log.query.filter(Log.isIn == 'True').all()
    return render_template('/LogSystem/logHistoryInfo.html', logList=logList)
