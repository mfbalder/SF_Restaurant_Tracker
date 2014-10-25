from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route("/")
def main_page():
	return render_template("index.html")

@app.route("/display_restaurant")
def display_restaurant():
	restaurant = request.args.get("restaurant")
	cuisine = request.args.get("cuisine")
	neighborhood = request.args.get("neighborhood")
	notables = request.args.get("notables").split(",")
	visited_status = request.args.get("visited")
	opinion = request.args.get("opinion")
	if not visited_status:
		visited_status = 0
	if not opinion:
		opinion = 0
	database.add_restaurant(restaurant, cuisine, neighborhood, visited_status, opinion)
	for n in notables:
		database.add_notable(restaurant, n.lower())

	return render_template("display_restaurant.html", 
		restaurant = restaurant,
		neighborhood = neighborhood,
		notables = notables)

if __name__ == "__main__":
	app.run(debug=True)