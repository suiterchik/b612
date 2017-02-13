# -*- coding: utf-8 -*-
from . import admin
from flask import request, redirect, render_template, send_from_directory, current_app, make_response, send_file
from flask.ext.login import login_required
import os
from datetime import datetime


@admin.route('/cloud')
@login_required
def cloud():
    sep = '@fuck_nvidia@'
    filename_list = os.listdir('cloud')
    filename_list.reverse()
    files = [{'name': filename.split(sep)[1],
              'url': '/download_file?filename=' + filename,
              'create_time': str(datetime.strptime(filename.split(sep)[0], '%Y-%m-%d %H-%M-%S')),
              } for filename in filename_list]
    return render_template('cloud.html', files=files)


@admin.route('/upload_file', methods=['POST'])
@login_required
def upload_file():
    f = request.files['file']
    f.save('cloud/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '@fuck_nvidia@' + f.filename)
    return redirect('/cloud')


@admin.route('/download_file')
@login_required
def download_file():
    filename = request.args['filename']
    path = '../cloud/'+filename
    response = make_response(send_file(path))
    response.headers["Content-Disposition"] = "attachment; filename=%s;" % filename.split('@fuck_nvidia@')[1]
    return response
