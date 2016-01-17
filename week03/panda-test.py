class Panda():
	def __init__(self, name, age, weight):
		self._name = name
		self._age = age
		self._weight = weight
	
	def eat(self, amount):
		self._weight += amount

	def sleep(self):
		self._age += 1

	def get_age(self):
		return self._age

	def get_weight(self):
		#Method za doobrabotvane | Ako se importva classa metodite s _ nqma da byde vkl
		pass

	def __str__(self):
		return "I am {0} and I am a proud Panda.\nMy age is {1} and my weight is {2}".format(self._name, self._age, self._weight)
	
	def __repr__(self):
		return self.__str__()

	def __hash__(self):
		return hash(self._name + str(self._age))
	
	def __eq__(self, other):
		return self._name == other._name


ivo = Panda("Ivo", 22, 90)
#print(dir(ivo))
#print(ivo._Panda__get_age())
#ivo.sleep()
#ivo.eat(20)
#ivo._age = 1
#print(ivo._age, ivo._weight)
#print(ivo.get_age())
#print(ivo)
rado = Panda ("Ivo", 22, 95)
print(ivo == rado)
print(hash(ivo))