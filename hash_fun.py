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
    self.p = random_prime_generator(self.size**2, self.size**3)

  def create(self):
    a = random.randint(1, self.p-1)
    b = random.randint(0, self.p-1)
    return lambda x: ((a * x + b) % self.p) % self.size

  def create_str_fun(self):
    a = random.randint(1, self.p-1)
    def hash(s):
      h = 5381
      for x in s:
        h = (((h*a) + ord(x)) % self.p) % self.size
      return h
    return hash

