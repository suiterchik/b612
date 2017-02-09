# -*- coding:utf-8 -*-
from flask import Blueprint

admin = Blueprint('b612', __name__)

from . import base, errors, auth
