from hash_fun import HashFunGenerator
m=30
hfgen = HashFunGenerator(m)
hash_fun = hfgen.create()
hash_fun_string = hfgen.stringify(hash_fun)
assert hash_fun_string("wena") == hash_fun_string("wena")