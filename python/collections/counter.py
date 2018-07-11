from collections import *

c = Counter('gallahad')
print c
# Counter({'a': 3, 'l': 2, 'h': 1, 'g': 1, 'd': 1})

c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print c
# Counter({'red': 4, 'blue': 2})

c = Counter(cats=4, dogs=8)
print c
# Counter({'dogs': 8, 'cats': 4})

c = Counter(a=4, b=2, c=0, d=-2)
print list(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']

print c
# Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})

print c.most_common()
# [('a', 4), ('b', 2), ('c', 0), ('d', -2)]

print c.most_common(2)
# [('a', 4), ('b', 2)]

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print c
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

print c.items()
# [('a', 3), ('c', -3), ('b', 0), ('d', -6)]
