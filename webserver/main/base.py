from . import admin
from flask import render_template, request, send_file
from webserver.model import Notes, DBSession
import math


@admin.route('/')
def index():
    page = request.args.get('page', default=1, type=int) - 1
    page_size = 10
    session = DBSession()
    notes = session.query(Notes).filter_by(status=1).order_by(Notes.id.desc()).offset(page).limit(page_size).all()
    max_page = int(math.ceil(1.0 * session.query(Notes).filter_by(status=1).count() / page_size))
    session.close()
    return render_template('index.html', notes=notes, page=page, max_page=max_page)


@admin.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')
