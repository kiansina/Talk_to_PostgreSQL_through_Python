import psycopg2
conn=psycopg2.connect(
      host='***********', database='*************', user='****************',password='*****************', connect_timeout=3)


cur=conn.cursor()
cur.execute('drop table if exists pythonfun cascade;')
cur.execute('select * from stop_words;')
row=cur.fetchone()
print(row)
