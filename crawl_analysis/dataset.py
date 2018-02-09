import sqlite3
import libnacl.public
import binascii
import pandas as pd

conn = sqlite3.connect('multichain_09_02_18.db')

def public_key(key):
    return str(key[10:]).encode('hex')

df = pd.read_sql_query("select * from multi_chain;", conn)
# print df.public_key_requester.apply(public_key).nunique() # 5641
print df.public_key_responder.apply(public_key).nunique() # 5784
# alice = str(df['public_key_requester'][0][10:]).encode('hex')
# print alice
# for row in df['public_key_requester']:
#     print str(row).encode('hex')
# print (c.fetchall());
# meta = c.execute("PRAGMA table_info('multi_chain')")
# for r in meta:
#     print r

# c.execute("select * from multi_chain")
# l = c.fetchone()
# print str(l[0][10:]).encode('hex')
# print l[0]


# c.execute('select * from multi_chain where {} = "{}"'.format('public_key_requester', l[0]))
# ll = c.fetchall()
# print len(ll)