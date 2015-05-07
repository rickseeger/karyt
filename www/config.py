
svrinfo = {
    'root': '/home/ubuntu/karyt/www',
    'ip': '172.30.0.115',
    'port': 80,
    'debug': True
}

dbinfo = {
  'user': 'root',
  'host': '127.0.0.1',
  'database': 'karyt',
}
pwd = open('/home/ubuntu/auth/mysql', 'r').read()
dbinfo['password'] = pwd
