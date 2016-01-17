from random import randint



class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "{} {} with max speed of: {}".format(self.car, self.model, self.max_speed)

    def __int__(self):
        return(self.max_speed)



class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.crashed = False

    def __str__(self):
        return "{} drives {} {} ".format(self.name, self.car.car, self.car.model)

    def __repr__(self):
        return self.__str__()



class Race():
	def __init__(self, drivers, crash_chance):
		self.drivers = [driver.name for driver in drivers]
		self.crash_chance = crash_chance
	

	def crash(self):
		for driver in self.drivers:
			num = randint(1, 10)
			if self.crash_chance * num > 5:
				driver.crashed = True
				return("Unfortunately, {} has crashed.".format(self.drivers.name))
	

	def race(self):
		places = []
		players = {}
		overall_success = []
		for driver in self.drivers:
			if driver.crashed is False:
				coef = driver.car.max_speed * randint(1, 10)
			else:
				coef = 0
			players[coef] = driver
			overall_success.append(coef)
		overall_success = overall_success.sort(reverse = True)
		for success in overall_success:
			places.append(players[success])
		return places


	def result(self):
		result = {}
		places = self.race()
		for driver in range(0, len(self.drivers)):
			if n == 0:
				result[places[0]] = 8
			elif n == 1:
				result[places[1]] = 6
			elif n == 2:
				result[places[2]] = 4
			else:
				result[places[n]] = 0
		return result



class Championship:
	def __init__(self, name, races_count):
		self.name = name
		self.races_count = races_count

class CLI:
	def __init__:
		pass
	