from flask import render_template, flash

from app import app


@app.route('/')
def wall():
    return render_template('Core/wall.html', title='Wall')
