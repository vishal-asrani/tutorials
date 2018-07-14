from itertools import *

print list(permutations(range(3)))
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

print list(permutations([1,2,3],2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print list(permutations('abc',2))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
