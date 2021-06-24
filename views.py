from flask import request, redirect, render_template, g
from datetime import datetime
from app import app
from tag import Tag
from IPython import embed

@app.route('/', methods=['GET'])
def show_tags():
    g.setdefault('image', app.config['config']['awesome_image']) # Flask.g: a way to pass var to a template
    g.setdefault('title', app.config['config']['title'])
    return render_template('index.html', tags=Tag.select())

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
        name=request.form['tag-name'],
        defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')

# Called by Javascript
@app.route('/tags/<tag>', methods=['DELETE'])
def remove_tag(tag):
    tag_to_remove = Tag.get(Tag.name == tag).delete_instance()

    return '', 204 # No need to return any content
