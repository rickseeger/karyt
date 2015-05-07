#!/usr/bin/env python

from config import dbinfo, svrinfo
from bottle import route, run, static_file, post, request
import mysql.connector


@route('/')
def home():
    return static_file('index.html', root=svrinfo['root'])


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=svrinfo['root'])


@post('/alias/add')
def add_alias():
    alias = request.forms.get('alias')
    pubkey = request.forms.get('pubkey')
    ip = request.environ.get('REMOTE_ADDR')
    query = (" REPLACE INTO aliases (alias, pubkey, ip, created) VALUES (%s, %s, %s, now()) ")
    vals = (alias, pubkey, ip)
    conn = mysql.connector.connect(**dbinfo)
    cursor = conn.cursor()
    cursor.execute(query, vals)
    conn.commit()
    cursor.close()
    conn.close()
    return static_file('landing.html', root=svrinfo['root'])


@route('/<alias>')
def get_alias(alias):
    query = (" SELECT pubkey FROM aliases "
             " WHERE alias = %s OR alias = %s")
    vals = (alias, alias)
    conn = mysql.connector.connect(**dbinfo)
    cursor = conn.cursor()
    cursor.execute(query, vals)
    pubkey = None
    for rec in cursor:
        pubkey = rec[0]
    cursor.close()
    conn.close()
    if (pubkey == None):
        return static_file('notfound', root=svrinfo['root'])
    else:
        return(pubkey)


# run server
run(host=svrinfo['ip'], port=svrinfo['port'], debug=svrinfo['debug'])

