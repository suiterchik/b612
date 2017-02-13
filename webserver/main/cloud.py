# -*- coding: utf-8 -*-
from . import admin
from flask import request, redirect, render_template
from flask.ext.login import login_required
import os
from datetime import datetime


@admin.route('/cloud')
def cloud():
    filename_list = os.listdir('cloud')
    filename_list.reverse()
    print filename_list[0].decode('gbk').encode('utf-8')
    files = [{'create_time': datetime.strptime(filename.split('@fuck_nvidia@')[0], '%Y-%m-%d %H-%M-%S').strftime('%Y-%m-%d %H:%M:%S'),
              'name': filename.split('@fuck_nvidia@')[1]}
             for filename in filename_list]
    return render_template('cloud.html', files=files)


@admin.route('/upload_file', methods=['POST'])
@login_required
def upload_file():
    f = request.files['file']
    f.save('cloud/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '@fuck_nvidia@' + f.filename)
    return redirect('/cloud')
