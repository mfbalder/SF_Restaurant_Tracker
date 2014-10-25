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

