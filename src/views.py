from flask import render_template, flash, session, redirect, url_for, request, jsonify
from flask_login import current_user

from app import app


@app.route('/')
def wall():
    return render_template('Core/wall.html', title='Wall')


@app.route('/get_username')
def get_username():
    response = {
        'username': current_user.username
    }
    return jsonify(response)


@app.errorhandler(404)
def unauthorized_error(e):
    flash('page not found')
    return render_template('Core/error.html', error=e), 404
