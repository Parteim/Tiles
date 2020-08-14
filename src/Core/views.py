from flask import render_template

from app import app


@app.route('/')
def core():
    return render_template('Base/base_template.html', message='Hi')
