# -*- coding:utf-8 -*-
__author__ = 'jinxiu.qi'
import sys
import ConfigParser
from flask.ext.script import Manager, Shell, Server
from webserver import create_app

reload(sys)
sys.setdefaultencoding('utf-8')

cf = ConfigParser.ConfigParser()
cf.read('b612.ini')
host = cf.get('webserver', 'host')
port = cf.get('webserver', 'port')
app = create_app()
manager = Manager(app)
server = Server(host=host, port=port)
manager.add_command("runserver", server)

if __name__ == "__main__":
    action = sys.argv[1]
    if action == "runserver":
        manager.run()

