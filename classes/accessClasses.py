from flask import render_template, Blueprint, request, flash, redirect, url_for
from .data.db import get_db

bp = Blueprint('access', __name__)


def get_class_info():
    db = get_db()
    classes = db.execute(
        "SELECT name, instructor, date, time FROM class ORDER BY date "
    ).fetchall()

    return classes

@bp.route('/')
def access():

    class_info = get_class_info()

    return render_template("home.html", classes=class_info)