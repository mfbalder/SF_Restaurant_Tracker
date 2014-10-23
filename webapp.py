from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main_page():
	return render_template("index.html")

@app.route("/display_restaurant")
def display_restaurant():
	restaurant = request.args.get("restaurant")
	neighborhood = request.args.get("neighborhood")
	to_try = request.args.get("to-try")
	return render_template("display_restaurant.html", 
		restaurant = restaurant,
		neighborhood = neighborhood,
		to_try = to_try)

if __name__ == "__main__":
	app.run(debug=True)