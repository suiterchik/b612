from . import admin


@admin.route('/')
def index():
    return '<h1>hello b612<h1>'
