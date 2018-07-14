dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
# {'a': 2, 'c': 6, 'b': 4, 'e': 10, 'd': 8}

dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)
# {'aa': 1, 'cc': 3, 'ee': 5, 'dd': 4, 'bb': 2}

new_dict_comp = {n:n**2 for n in range(10) if n%2 == 0}
print(new_dict_comp)
# {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}