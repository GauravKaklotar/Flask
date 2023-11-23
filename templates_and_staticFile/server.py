'''
		################################# Flask Rendering Templates. #################################
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
	return render_template("about.html", sites=sites)

@app.route("/contact/<role>")
def contact(role):
	return render_template("contact.html", person=role)


# @app.route("/<name>")
# def welcome(name):
# 	return render_template("welcome.html", name=name)

if __name__ == "__main__":
	app.run(debug=True)
'''


		################################# CSRF Tokens #################################
from flask import Flask, render_template, request 
from flask_wtf import CSRFProtect 

app = Flask(__name__) 
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf = CSRFProtect(app) 


# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route("/protected_form", methods=['GET', 'POST']) 
def protected_form(): 
	if request.method == 'POST': 
		name = request.form['Name'] 
		return (' Hello ' + name + '!!!') 
	return render_template('index.html') 

@app.route("/unprotected_form", methods=['GET', 'POST']) 
def unprotected_form(): 
	if request.method == 'POST': 
		name = request.form['Name'] 
		return (' Hello ' + name + '!!!') 
	return render_template('index.html') 

if __name__ == '__main__': 
	app.run(debug=True)
