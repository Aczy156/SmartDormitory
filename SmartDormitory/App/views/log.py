from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Log

logBlue = Blueprint('logBlue', __name__)


@logBlue.route('/LogSystem/logHistoryInfo', methods=['POST', 'GET'])
def logHistoryInfo():

    return None


@logBlue.route('/Log/selectHistory', methods=['POST', 'GET'])
def dormitoryPayment():
    return None


