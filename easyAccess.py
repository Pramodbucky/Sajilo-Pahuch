from flask import Flask, request, render_template, \
 make_response, redirect, url_for
from os import urandom, path
from hashlib import sha512
from functions import addData, vaildateCreds, findNearestService

webApp = Flask(__name__)

session = {}
webApp.secret_key = urandom(64)
webApp.template_folder = path.join(webApp.root_path, 'dynamicFiles')
webApp.static_folder = path.join(webApp.root_path, 'staticFiles')


@webApp.route('/', methods=['GET', 'POST'])
def mainPage():
    if request.method == 'GET':
        if not session:
            return render_template('index.html',
                                   session=session)
        else:
            return render_template('application.html',
                                   session=session)
    else:
        if session:
            print(request.form)
            if 'location' in request.form:
                userLoc = request.form['location'].split(';')
                userLoc = {'lat': float(userLoc[0]),
                           'lon': float(userLoc[1])}
                return str(findNearestService(userLoc))
            else:
                return 'Loction not Provided.'
        else:
            return 'Access Denied!'


@webApp.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return render_template('login.html',
                               session=session)
    else:
        if vaildateCreds(request.form):
            session['username'] = request.form['username']
            return redirect('/')
        return '<h1 align="center"> Access Denied! </h1>'


@webApp.route('/logout', methods=['POST'])
def logoutFunc():
    session.pop('username', None)
    return redirect(url_for('mainPage'))


@webApp.route('/register', methods=['GET', 'POST'])
def registerPage():
    if request.method == 'GET':
        return render_template('register.html',
                               session=session)
    else:
        addData(request.form)
        return 'Done.'


@webApp.route('/base')
def hhvgc():
    return render_template('base.html',
                           session=session)


@webApp.route('/index')
def SendBase():
    return render_template('index.html',
                           session=session)
