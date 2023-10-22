from app.students import student_blueprint


# use blueprint to collect related urls
@student_blueprint.route('/hello', endpoint='hello')
def sayhello():
    return '<h1 style="color:red; text-align:center">  Hello world from flask MVT</h1>'
