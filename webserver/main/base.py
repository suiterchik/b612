from . import admin
from flask import render_template


@admin.route('/')
def index():
    notes = []
    page = 1
    max_page = 10
    return render_template('index.html', notes=notes, page=page, max_page=max_page)
