import psycopg2
import hidden
import time
import myutils
import requests
import json


secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()


sql = '''
CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);
'''
print(sql)
cur.execute(sql)

for i in range(1,101):
    url='https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
    print(url)
    response = requests.get(url)
    print('11111111111111', response)
    text = response.text
    sql='INSERT INTO pokeapi (body) VALUES (%s);'
    cur.execute(sql, (text, ))

conn.commit()
cur.close()
