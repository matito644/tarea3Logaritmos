import math
from hash_fun import HashFunGenerator
from bitarray import bitarray

# n es el número esperado de objetos en el filtro de bloom
# fp es la probabilidad deseada de un falso positivo
class BloomFilter():
	def __init__(self, n, fp):
		# número óptimo para m
		self.m = int(-(n * math.log(fp))/(math.log(2)**2))
		# número óptimo de funciones de hash
		self.k = int((self.m/n) * math.log(2))
		# arreglo M de tamaño m
		self.M = bitarray(self.m)
		# parte en cero
		self.M.setall(0)
		# funciones de hash
		self.hashFunctions = []
		for i in range(self.k):
			fun = HashFunGenerator(self.m)
			self.hashFunctions.append(fun)

	# insertar un elemento en el filtro de bloom
	def add(self, string):
		index = 0
		for i in range(self.k):
			# aplicar la función de hash
			val = self.hashFunctions[index].hashForStrings(string)
			# M[val] queda True
			self.M[val] = True
			# para utilizar la siguiente función de hash
			index+=1

	# verificar si un elemento estaba en el filtro
	def check(self, string):
		index = 0
		for i in range(self.k):
			# aplicar la función de hash
			val = self.hashFunctions[index].hashForStrings(string)
			# si M[val] era False, es seguro que no estaba
			if self.M[val] == False:
				return False
			index+=1
		# posiblemente estaba
		return True

class BloomFilterWithoutKandM(BloomFilter):
	def __init__(self, k, m):
		self.k = k
		self.m = m
		self.M = bitarray(self.m)
		# parte en cero
		self.M.setall(0)
		# funciones de hash
		self.hashFunctions = []
		for i in range(self.k):
			fun = HashFunGenerator(self.m)
			self.hashFunctions.append(fun)