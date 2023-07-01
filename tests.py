from main import BloomFilter
import csv
import time

fp = 0.1
PATH = "Popular-Baby-Names-Final.csv"
count = 93890


csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
bloomy = BloomFilter(count, fp)
for name in csv_file:
    bloomy.add(name[0])
    
def generate_n_names(N, path=PATH):
    csv_file = csv.reader(open(f'{path}', "r"), delimiter=",")
    return [row[0] for row, _ in zip(csv_file, range(N))]

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
        if name[0] in list_of_names:
            l[name[0]] = True
    return l


def time_test(n = 1000, trials = 3):
    prom_fil = 0
    prom_normal = 0
    for _ in range(trials):
        lista = generate_n_names(n)
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
    print(f"En {trials} intentos con una lista de {n} elementos")
    print(f"Promedio filtro de bloom --> {prom_fil:.3f}s")
    print(f"Promedio busqueda normal --> {prom_normal:.3f}s")

if __name__ == "__main__":
    time_test(trials=20)