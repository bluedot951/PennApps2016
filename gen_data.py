import psycopg2
import urlparse
import random

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://gxspomxmufoybd:dskomEuwa9JYaxf8Jd7h8JYVKo@ec2-54-221-253-117.compute-1.amazonaws.com:5432/d62ndf8grb25cb')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cursor = conn.cursor()
# for i in range(289):
#   cursor.execute(
#       'INSERT INTO "GOOG_price_history"(id, stamp, price) VALUES (%s, now(), %s);' % (i, (0.25 + random.uniform(-0.05, 0.05)))
#   )
#   cursor.execute(
#       'INSERT INTO "GTHB_price_history"(id, stamp, price) VALUES (%s, now(), %s);' % (i, (0.25 + random.uniform(-0.05, 0.05)))
#   )
#   cursor.execute(
#       'INSERT INTO "PENN_price_history"(id, stamp, price) VALUES (%s, now(), %s);' % (i, (0.25 + random.uniform(-0.05, 0.05)))
#   )


cursor.execute(
    'INSERT INTO entity(id, username, balance) VALUES (DEFAULT, "%s", 100.00);' % ('wayway_buffet69')
)


conn.commit()