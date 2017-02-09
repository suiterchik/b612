from . import admin
from flask import request, redirect, render_template
from webserver.model import DBSession, Notes
from flask.ext.login import login_required


@admin.route('/cloud')
def cloud():
    article_list = []
    return render_template('cloud.html', article_list=article_list)


@admin.route('/upload_file', methods=['POST'])
@login_required
def upload_file():
    f = request.files['file']
    f.save('logs/' + f.filename)
    return redirect('/cloud')
