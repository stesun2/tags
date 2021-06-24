import sys
from app import app, db
from os.path import abspath, dirname, join
base_path  = dirname(abspath(__file__))
sys.path.insert(1, sys.path[0])
sys.path.insert(1, join(base_path, 'lib'))
sys.path.insert(1, join(base_path, 'models'))
import views
from tag import Tag  # a Peewee DB model

if __name__ == '__main__':
    db.create_tables([Tag], safe=True)
    app.run('0.0.0.0','5555', debug=True)
