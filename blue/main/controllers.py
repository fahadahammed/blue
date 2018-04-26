from flask import Blueprint, request, redirect, session, url_for

main = Blueprint("main", __name__, url_prefix='/main')


@main.route("/", methods=["GET", "POST"])
def mainindex():
    if request.method == "GET":
        name = str(session.get('username'))
        name2 = name + 'mainindex'
        print(name,'main')
        return name2


@main.route("/mainindex2", methods=["GET", "POST"])
def mainindex2():
    if request.method == "GET":
        name = str(session.get('username'))
        print(name, 'mainindex2')
        return redirect(url_for('home.homeindex'))