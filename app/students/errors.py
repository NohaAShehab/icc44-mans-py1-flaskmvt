
from flask import render_template
from app.students import student_blueprint
@student_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('errors/page_not_found.html')
