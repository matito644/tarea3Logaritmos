# Python 3 program to build Bloom Filter
# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import math
import mmh3
from bitarray import bitarray
#Un poquito de teoria primero
# num es el numero esperado de objetos en el filtro de bloom
# fp es la proba de ser falso positivo
class BloomFilter():
	def __init__(self, num: int, fp: float):
		# False possible probability in decimal
		self.fp_prob = fp

		# Size of bit array to use
		self.size = self.get_size(num, fp)

		# number of hash functions to use
		self.hash_count = self.get_hash_count(self.size, num)

		# Bit array of given size
		self.bit_array = bitarray(self.size)

		# initialize all bits as 0
		self.bit_array.setall(0)

	def add(self, item):
		'''
		Add an item in the filter
		'''
		digests = []
		for i in range(self.hash_count):

			# create digest for given item.
			# i work as seed to mmh3.hash() function
			# With different seed, digest created is different
			digest = mmh3.hash(item, i) % self.size
			digests.append(digest)

			# set the bit True in bit_array
			self.bit_array[digest] = True

	def check(self, item):
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			if self.bit_array[digest] == False:
				return False
		return True

	#@classmethod
	def get_size(self, n, p):
		m = -(n * math.log(p))/(math.log(2)**2)
		return int(m)

	#@classmethod
	def get_hash_count(self, m, n):
		k = (m/n) * math.log(2)
		return int(k)
