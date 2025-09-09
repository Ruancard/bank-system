import psycopg2
import psycopg2.extras
import random



hostname = 'localhost'
database = 'banco'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            
            select_script = 'SELECT * FROM accounts WHERE name = %s'
            select_record = ('ruan ardoso moreira',)
            cur.execute(select_script, select_record) 
            record = cur.fetchall()
            try:
                print(f'{record[0]}')
            
            except IndexError:
                print('erro')


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
