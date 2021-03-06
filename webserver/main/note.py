from . import admin
from flask import request, redirect
from webserver.model import DBSession, Notes
from flask.ext.login import login_required
from datetime import datetime


@admin.route('/new_note', methods=['POST'])
@login_required
def new_note():
    content = request.form.get('content')
    note = Notes(content=content, status=1, create_time=datetime.now())
    session = DBSession()
    session.add(note)
    session.commit()
    session.close()
    return redirect('/')


@admin.route('/delete_note')
@login_required
def delete_note():
    session = DBSession()
    note = session.query(Notes).filter_by(id=request.args.get('id')).first()
    note.status = 0
    session.commit()
    session.close()
    return redirect('/')
