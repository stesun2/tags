import sys
from os.path import join, dirname, abspath
sys.path.insert(1, join(dirname(abspath(__file__)), '..'))
from config import load_config
from app import db, dbname
from sqlite3 import connect

def load_schema():
    conn = connect(dbname)
    schema = open('db/schema.sql', 'r').read()
    conn.execute(schema)
    conn.close

def seed():
    conn = connect(dbname)
    f = open('db/seed.sql', 'r')
    for sql in f:
      conn.execute(sql)
      conn.commit()
    f.close() 
    conn.close
