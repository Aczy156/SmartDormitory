from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, User

userBlue = Blueprint('userBlue', __name__)


@userBlue.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        result = User.query.filter(User.username == username, User.password == password).first()
        if result:
            userItem = {}
            userItem['username'] = result.username
            userItem['userPicture'] = result.userPicture
            userItem['roomId'] = result.roomId

            session['user'] = userItem
            return render_template('index.html')

        else:
            return render_template('login.html', message='用户名不存在或密码错误！')


# query
@userBlue.route('/getuser')
def getuser():
    result = User.query.filter(User.username == 'a').first()
    return result.username


@userBlue.route('/index')
def index():
    return render_template('index.html')


@userBlue.route('/account')
def account():
    return render_template('index.html')


# login
@userBlue.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('userblue.login'))


# register
@userBlue.route('/register', methods=['POST', 'GET'])
def regist():
    user = User()
    user.username = request.form.get('register_username')
    user.password = request.form.get('register_password')
    user.email = request.form.get('register_email')

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('userBlue.login'))


# select
@userBlue.route('/User/info', methods=['POST', 'GET'])
def myselect():
    item = session.get('user')
    user = User.query.filter(User.username == item.get("username")).first()
    return render_template('UserSystem/userInfo.html', user=user)


# UserInfo
# GET get info
# POST change
@userBlue.route('/User/updateUserInfo', methods=['POST', 'GET'])
def myupdate():
    item = session.get('user')
    user = User.query.filter(User.username == item.get("username")).first()
    if request.method == 'GET':
        return render_template('UserSystem/updateUserInfo.html', user=user)
    else:
        user.email = request.form.get('updateUserInfo_email')
        user.phone = request.form.get('updateUserInfo_phone')
        user.password = request.form.get('updateUserInfo_password')
        user.introduction = request.form.get('updateUserInfo_introduction')
        db.session.add(user)
        db.session.commit()
        return render_template('UserSystem/updateUserInfo.html', user=user, message='修改成功')
