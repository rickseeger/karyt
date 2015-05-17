#!/usr/bin/env python

from config import dbinfo, svrinfo
from bottle import route, run, static_file, post, request
import mysql.connector
from common import rand_string, send_confirmation


@route('/')
def home():
    return static_file('index.html', root=svrinfo['root'])


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=svrinfo['root'])


@route('/confirm/<key>')
def confirm(key):
    query = (" UPDATE aliases SET confirmed = 1 WHERE confirmkey = %s ")
    vals = (key,)
    conn = mysql.connector.connect(**dbinfo)
    cursor = conn.cursor()
    cursor.execute(query, vals)
    conn.commit()
    cursor.close()
    conn.close()
    return static_file('alias_confirmed.html', root=svrinfo['root'])


@post('/alias/add')
def add_alias():
    alias = request.forms.get('alias')
    pubkey = request.forms.get('pubkey')
    ip = request.environ.get('REMOTE_ADDR')
    confirmkey = rand_string(32)
    query = (" REPLACE INTO aliases (alias, pubkey, ip, created, confirmed, confirmkey) "
             " VALUES (%s, %s, %s, now(), 0, %s) ")
    vals = (alias, pubkey, ip, confirmkey)
    conn = mysql.connector.connect(**dbinfo)
    cursor = conn.cursor()
    cursor.execute(query, vals)
    conn.commit()
    cursor.close()
    conn.close()
    send_confirmation(alias, confirmkey)
    return static_file('alias_created.html', root=svrinfo['root'])


@route('/<alias>')
def get_alias(alias):
    query = (" SELECT pubkey FROM aliases "
             " WHERE alias = %s "
             " AND confirmed = 1 " )
    vals = (alias, )
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

