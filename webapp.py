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

	if not restaurant or not cuisine or not neighborhood:
		return "Please provide a restaurant, cuisine, and neighborhood."
		
	if not visited_status:
		visited_status = 0
	if not opinion:
		opinion = 0

	add_resto = database.add_restaurant(restaurant, cuisine, neighborhood, visited_status, opinion)
	if add_resto != 0:
		for n in notables:
			database.add_notable(restaurant, n.lower())

		return "<h3>%s has been added!</h3>" % restaurant
	else:
		return "<h3>%s is already in the system.</h3>" % restaurant

	# return render_template("display_restaurant.html", 
	# 	restaurant = restaurant,
	# 	neighborhood = neighborhood,
	# 	notables = notables)

@app.route("/display_unvisited_restaurants")
def display_unvisited_restaurants():
	restos_dict = database.get_unvisited_restaurants()
	print restos_dict
	return render_template("display_unvisited_restaurants.html", restos_dict=restos_dict)



if __name__ == "__main__":
	app.run(debug=True)