from main import BloomFilter
import csv
import time
import matplotlib.pyplot as plt
fp = 0.1
PATH = "Popular-Baby-Names-Final.csv"
count = 93890


csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
bloomy = BloomFilter(count, fp)
for name in csv_file:
    bloomy.add(name[0])

#TODO: Hacer que genere nombres de manera aleatoria!
def generate_n_distinct_names(N, path=PATH) -> list:
    csv_file = csv.reader(open(f'{path}', "r"), delimiter=",")
    return [row[0] for row, _ in zip(csv_file, range(N))]

def generate_n_distinct_names_with_a_ratio(N, r) -> list:
    ...

def query_filter_for_n_names(list_of_names) -> dict:
    l = {}
    for name in list_of_names:
        val = bloomy.check(name)
        l[name] = val
    return l

def query_for_n_names(list_of_names):
    l = {}
    csv_file = csv.reader(open(f'{PATH}', "r"), delimiter=",")
    for name in csv_file:
        l[name[0]] = name[0] in list_of_names
    return l


def time_test(n = 1000, trials = 3):
    prom_fil = 0
    prom_normal = 0

    for _ in range(trials):
        lista = generate_n_distinct_names(n)
        start = time.perf_counter()

        query_filter_for_n_names(lista)
        stop = time.perf_counter()
        prom_fil += (stop-start)

        start = time.perf_counter()
        query_for_n_names(lista)
        stop = time.perf_counter()
        prom_normal += (stop-start)
    
    prom_fil = prom_fil/trials
    prom_normal = prom_normal/trials
    #print(f"En {trials} intentos con una lista de {n} elementos")
    #print(f"Promedio filtro de bloom --> {prom_fil:.3f}s")
    #print(f"Promedio busqueda normal --> {prom_normal:.3f}s")
    return (prom_fil, prom_normal)

def test_graph_mean_time_in_range(max = 8):
    l = []
    for n in (2**k for k in range(max)):
        l+= [time_test(n=n, trials=3)]
    l = list(zip(*l))
    plt.scatter([2**k for k in range(max)], l[0], color='red')
    plt.scatter([2**k for k in range(max)], l[1], color='blue')
    plt.xscale('log')
    #plt.show()
    plt.savefig('bad-graph.png')

def test_results_with_ratio(n, r):
    names = generate_n_distinct_names_with_a_ratio(n,r)
    results = query_filter_for_n_names(names)
    results2compare = query_for_n_names(names)
    
if __name__ == "__main__":
    test_graph_mean_time_in_range()