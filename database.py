import sqlite3

CONN = None
DB = None

def connect():
	global CONN, DB
	CONN = sqlite3.connect("restaurants.db")
	DB = CONN.cursor()

def add_restaurant(restaurant, cuisine, neighborhood, have_visited, opinion):
	connect()
	query = """INSERT INTO restaurants VALUES (?, ?, ?, ?, ?)"""
	DB.execute(query, (restaurant, cuisine, neighborhood, have_visited, opinion))
	CONN.commit()
	print "%s has been added" % restaurant

def add_notable(restaurant, notable):
	connect()
	query = """INSERT INTO notables VALUES (?, ?)"""
	DB.execute(query, (restaurant, notable))
	CONN.commit()
	print "Your %s notable has been added to %s" % (notable, restaurant)

def get_unvisited_restaurants():
	connect()
	query = """SELECT name, cuisine, neighborhood, notable_food FROM restaurants join notables ON 
		(restaurants.name = notables.restaurant_name) WHERE restaurants.visited_yet = 0"""
	DB.execute(query)
	resto_list = DB.fetchall()
	d = {}
	# print resto_list
	for resto in resto_list:
		name, cuisine, neighborhood, notable_food = resto
		if name not in d:
			d[name] = {"cuisine": cuisine, "neighborhood": neighborhood, "notable_food": [notable_food]}
		else:
			d[name]["notable_food"].append(notable_food)
	return d




