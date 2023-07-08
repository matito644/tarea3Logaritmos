import csv
import time
import matplotlib.pyplot as plt
from main import BloomFilter

# crear el filtro de Bloom
bloomFilter = BloomFilter(93889, 0.1)
print(bloomFilter.M)

# leer los csv
csv_names = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
csv_movies = csv.reader(open('Film-Names.csv', "r"), delimiter=",")

count = 0
# insertar los nombres en el filtro
for row in csv_names:
    if row[0] == "Name":
        continue
    bloomFilter.add(row[0])

print(bloomFilter.M)
