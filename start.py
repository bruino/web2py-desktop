import logging
from threading import Thread, Lock
from time import sleep
from contextlib import redirect_stdout
from io import StringIO
import subprocess

import webview

logger = logging.getLogger(__name__)

url = 'localhost'
port = 9000

def url_ok(url, port):
    # Use httplib on Python 2
    try:
        from http.client import  HTTPConnection
    except ImportError:
        from httplib import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request('GET', '/')
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception('Server not started')
        return False

def run_server():
    subprocess.call('python web2py.py -a %s -i %s -p %s' %('you-password-admin', url, port))

if __name__ == '__main__':
    logger.debug('Starting server')
    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    logger.debug('Server started')
    
    window = webview.create_window('Web2py App', 'http://localhost:9000/')
    webview.start()
