from flask import *
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def empty_route():
	return render_template("main.html")
