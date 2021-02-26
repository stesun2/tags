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
    with open('db/seed.sql', 'r') as f:
      conn.executescript( f.read() )
    conn.commit()
    conn.close
