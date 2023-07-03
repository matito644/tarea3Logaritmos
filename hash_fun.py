import random
## podria ser el prime tester que vimos en clases
def is_prime(num):
    for k in range(2,int(num**0.5)+1):
        if num%k==0:
            return False
    return True

## Algorimto tipo Las Vegas, toma uno al azar en un intervalo de ahí ve que vola
def random_prime_generator(ini, end):
  while True:
    p = random.choice(range(ini, end))
    if is_prime(p):
      return p
   
  
class HashFunGenerator():
  def __init__(self, m):
    self.cache = set()
    self.size = m

  def create(self):
    p = random_prime_generator(self.size**2, self.size**3)
    self.cache.add(p)
    a = random.randint(1, p-1)
    b = random.randint(0, p-1)
    return lambda x: ((a * x + b) % p) % self.size

  def stringify(self, fun):
    return lambda s: sum((fun(ord(char)) for char in s))