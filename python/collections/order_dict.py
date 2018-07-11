from collections import *

dict1 = {}
dict1['name'] = "Vishal"
dict1['age'] = 28
dict1['city'] = "Mumbai"
print("dict1: ",dict1)

order_dict1 = OrderedDict()
order_dict1['name'] = "Vishal"
order_dict1['age'] = 28
order_dict1['city'] = "Mumbai"
order_dict1['nationality'] = "Indian"

print("order_dict1: ",order_dict1)

order_dict1.popitem()

print("order_dict1: ",order_dict1)

order_dict1.popitem(last=False)

print("order_dict1: ",order_dict1)

# output:
# ('dict1: ', {'city': 'Mumbai', 'age': 28, 'name': 'Vishal'})
# ('order_dict1: ', OrderedDict([('name', 'Vishal'), ('age', 28), ('city', 'Mumbai'), ('nationality', 'Indian')]))
# ('order_dict1: ', OrderedDict([('name', 'Vishal'), ('age', 28), ('city', 'Mumbai')]))
# ('order_dict1: ', OrderedDict([('age', 28), ('city', 'Mumbai')]))