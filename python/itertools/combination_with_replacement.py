from itertools import *

print list(combinations_with_replacement(range(3), 2))
# [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

print list(combinations_with_replacement('abc', 2))
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

print list(combinations_with_replacement('abc', 3))
# [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), 
# ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')]