from collections import ChainMap

default_connection = {'host':'localhost', 'port': 4567}
connection = {'port':5678}
conn = ChainMap(connection,default_connection)
print(conn['port'])
print(conn['host'])

print(conn.maps)

conn['host'] = 'packtpub.com'
print(conn.maps)

del conn['port']
print(conn.maps)
print(conn['port'])
print(conn.maps)
print(dict(conn))