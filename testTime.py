from main import BloomFilter
import csv
import time
import random
import matplotlib.pyplot as plt


# crear el filtro de Bloom
bloomFilter = BloomFilter(93889, 0.1)

# leer los csv
csv_names = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
csv_movies = csv.reader(open('Film-Names.csv', "r"), delimiter=",")

# insertar los nombres en el filtro
for row in csv_names:
    if row[0] == "Name":
        continue
    bloomFilter.add(row[0])

# Se insertan nombres aleatorios en la lista para hacer las búsquedas
def generateRandomNames(N, path='Popular-Baby-Names-Final.csv'):
    l = []
    list_names = list(csv.reader(open(path, "r"), delimiter=","))
    for i in random.sample(range(1, 93889), N):
        l.append(list_names[i][0])
    return l

# buscarlo en el filtro
def checkFilter(names):
    for name in names:
        bloomFilter.check(name)
    return 0

# buscarlo sin el filtro
def checkNormal(names):
    # para cada nombre de la lista generada
    for name in names:
        # buscarlo en el csv
        csv_names = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        for row in csv_names:
            # cuando lo encuentra sale del for
            if name == row[0]:
                break
    return 0

# medir el tiempo
def time_test(n = 1000, trials = 3):
    prom_fil = 0
    prom_normal = 0
    for _ in range(trials):
        lista_nombres = generateRandomNames(n)
        # primero con el filtro
        start = time.perf_counter()
        checkFilter(lista_nombres)
        stop = time.perf_counter()
        prom_fil += (stop-start)
        # ahora sin el filtro
        start = time.perf_counter()
        checkNormal(lista_nombres)
        stop = time.perf_counter()
        prom_normal += (stop-start)
    # tiempos promedios
    prom_fil = prom_fil/trials
    prom_normal = prom_normal/trials
    return (prom_fil, prom_normal)

# graficar los tiempos
def gogoPlot(min = 7, max = 16):
    l = []
    for n in (2**k for k in range(min, max)):
        l+= [time_test(n=n, trials=3)]
    l = list(zip(*l))
    fig, ax = plt.subplots()
    ax.scatter([2**k for k in range(min, max)], l[0], color='red')
    ax.scatter([2**k for k in range(min, max)], l[1], color='blue')
    ax.set_xscale('log', base=2)
    fig.suptitle("Búsquedas Filtro de Bloom y búsqueda secuencial")
    plt.setp(ax, xlabel="Cantidad de nombres", ylabel="Tiempo (segundos)")
    plt.legend(("Filtro de Bloom","Secuencial"),fontsize=7, loc="upper left")
    ax.set_facecolor((0.95,0.95,0.95))
    plt.savefig('graficoTiempos.png', dpi=200)
    # plt.show()

if __name__ == "__main__":
    gogoPlot()
