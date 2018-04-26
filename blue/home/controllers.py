from flask import Blueprint, request, redirect, session, url_for

home = Blueprint("home", __name__, url_prefix='/home')


@home.route("/", methods=["GET", "POST"])
def homeindex():
    if request.method == "GET":
        session['username'] = "Titan"
        name = str(session.get('username'))
        name2 = name + 'homeindex'
        print(name, 'home')
        return name2


@home.route("/homeindex2", methods=["GET", "POST"])
def homeindex2():
    if request.method == "GET":
        name = str(session.get('username'))
        print(name, 'homeindex2')
        return redirect(url_for('main.mainindex'))