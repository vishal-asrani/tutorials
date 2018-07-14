from itertools import *

print list(combinations(range(3), 2))
# [(0, 1), (0, 2), (1, 2)]

print list(combinations('abc', 2))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

print list(combinations('abc', 3))
# [('a', 'b', 'c')]
