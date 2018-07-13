from collections import *

d = defaultdict(lambda: "any default value")

d["name"] = "Vishal"
d["age"] = 28
print d["name"]
# Vishal

print d["age"]
# 28

print d["city"]
# any default value


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
	d[k].append(v)

print d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1

print d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]