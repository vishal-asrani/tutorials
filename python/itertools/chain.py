from itertools import *

a = [0,1,2,3,4,5]
b = ['zero', 'one', 'two', 'three', 'four', 'five']
c = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(chain(a,b,c)))
# [0, 1, 2, 3, 4, 5, 'zero', 'one', 'two', 'three', 'four', 'five', 'a', 'b', 'c', 'd', 'e', 'f']

print(list(chain(a[0:],b[:1],c[0:2])))
# [0, 1, 2, 3, 4, 5, 'zero', 'a', 'b']