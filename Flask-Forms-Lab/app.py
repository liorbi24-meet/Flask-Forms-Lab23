from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


usernames_and_passwords = {"lior" : "1234", "daria" : "2017", "jihad" : "1729", "sirgey" : "IasaFoodIsGood"}
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		for i in usernames_and_passwords:
			if i == username and usernames_and_passwords[i] == password:
				return redirect(url_for('home'))
			else:
				return render_template('login.html', username = username, password = password)

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html', freinds = facebook_friends)


@app.route("/friend_exists/<string:name>")
def freinds_exist(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', bool = "true")
	else:
		return render_template('friend_exists.html', bool = "false")

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
'"'