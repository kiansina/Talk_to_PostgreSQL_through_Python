import psycopg2
import hidden

secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

sql = 'create TABLE pythonseq (iter INTEGER, val INTEGER);'
print(sql)
cur.execute(sql)



value = 126780
for i in range(300) :
    sql= 'insert into pythonseq (iter, val) values ({}, {});'.format(i+1,value)
    cur.execute(sql)
    #print(i+1, value, 'Inserted')
    value = int((value * 22) / 7) % 1000000
    if i%50==0:
        conn.commit()
