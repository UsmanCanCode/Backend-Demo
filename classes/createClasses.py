from flask import render_template, Blueprint, request, flash, redirect, url_for
from .data.db import get_db

bp = Blueprint('create', __name__)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        class_name = request.form.get("class_name")
        instructor = request.form.get('instructor')
        scheduled_date = request.form.get("scheduled_date")
        scheduled_time = request.form.get("scheduled_time")
        db = get_db()
        error = None

        if not (class_name and instructor and scheduled_date and scheduled_time):
            error ="Please fill all the fields!"
        if error == None:
            try:
                db.execute(
                    "INSERT INTO class (name, instructor, date, time) VALUES (?,?,?,?)",
                    (class_name, instructor, scheduled_date, scheduled_time),
                )
                db.commit()
            except db.Error:
                error= "datbase error!"
            else: 
                return redirect("/")

        flash(error)

    return render_template('/create.html')