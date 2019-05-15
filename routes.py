import random

ids = []

def new_id(ids):
	new = random.randrange(1000, 10000)
	if new in ids:
		return new_id(ids)
	return new

def diff(time_arr, time_dep):
	arr_mins = time_arr.hr * 60 + time_arr.mm
	mins_diff = time_dep.hr * 60 + time_dep.mm
	return arr_mins - mins_diff

def get_available_routes(year, routes):
	for route in routes:
		if route.depart_time.year == 2013:
			route.print_route()

def get_flights(station, routes):
	for route in routes:
		if route.depart_station == station:
			route.print_route()

def short_flights(time, routes):
	for route in routes:
		if diff(route.arrival_time, route.depart_time) < time:
			route.print_route()


class Time:
	def __init__(self, hr, mm, day, month, year):
		self.hr = hr
		self.mm = mm
		self.day = day
		self.month = month
		self.year = year

class Route:
	def __init__(self, id, depart_station, arrival_station, depart_time, arrival_time):
		self.id = id
		self.depart_station = depart_station
		self.arrival_station = arrival_station
		self.depart_time = depart_time
		self.arrival_time = arrival_time
		ids.append(id)

	def print_route(self):
		print "====================== Route No. " + str(self.id) + " ======================"
		print "--- Departure from:\t" + str(self.depart_station) + "\tat: " + \
			str(self.depart_time.hr) + ":" + str(self.depart_time.mm) + " " + \
			str(self.depart_time.day) + "/" + str(self.depart_time.month) + "/" + \
			str(self.depart_time.year)
		print "--- Arrival in:\t\t" + str(self.arrival_station) + "\t\tat: " + \
			str(self.arrival_time.hr) + ":" + str(self.arrival_time.mm) + " " + \
			str(self.arrival_time.day) + "/" + str(self.arrival_time.month) + "/" + \
			str(self.arrival_time.year)
		print "============================================================\n"

routes = [
	Route(new_id(ids), "Bucuresti", "Madrid", Time(21, 55, 5, 10, 1996), Time(23, 35, 5, 10, 1996)),
	Route(new_id(ids), "Tenerife", "Ibiza", Time(21, 55, 5, 10, 2010), Time(23, 35, 5, 10, 2010)),
	Route(new_id(ids), "Valencia", "Geneva", Time(20, 55, 5, 10, 2013), Time(22, 45, 5, 10, 2013)),
	Route(new_id(ids), "Bucuresti", "Craiova", Time(19, 55, 7, 11, 2015), Time(20, 45, 7, 11, 2015))]

# print "\nAvailable routes: \n"
# for route in routes:
# 	route.print_route()

print "*********************"
print "Routes in 2013:"
print "*********************"
get_available_routes(2013, routes)

print "*********************"
print "Routes from Bucharest:"
print "*********************"
get_flights("Bucuresti", routes)

print "*********************"
print "Short flights (<1h):"
print "*********************"
short_flights(60, routes)