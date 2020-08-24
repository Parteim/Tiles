from flask import render_template, flash, session, redirect, url_for, request, jsonify

from app import app


@app.route('/')
def wall():
    return render_template('Core/wall.html', title='Wall')


# @app.errorhandler(401)
# def unauthorized_error(e):
#     print(request.args.add())
#     flash('Need authorisation')
#     return redirect(url_for('User.sign-in'))


@app.errorhandler(404)
def unauthorized_error(e):
    flash('page not found')
    return render_template('Core/error.html', error=e)
