import random

# función de hash
class HashFunGenerator():
    def __init__(self, m):
        self.m = m
        # primo
        self.p = 10**9 + 9
        self.listOfa_i = []
        # nombre más largo tiene 15 letras
        for i in range(15):
            a = random.randint(1, self.p-1)
            self.listOfa_i.append(a)
        self.b = random.randint(0, self.p-1)

    # según apunte
    def hashForStrings(self, string):
        sum = 0
        index = 0
        for i in string:
            sum += self.listOfa_i[index] * ord(i)
            index+=1
        return ((self.b + sum) % self.p) % self.m
