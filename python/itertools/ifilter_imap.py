from itertools import *

print list(ifilter(lambda x: x%2, range(10)))
# [1, 3, 5, 7, 9]

n = [1,2,3,4]
print list(imap(lambda x:x**2,n))
# [1, 4, 9, 16]