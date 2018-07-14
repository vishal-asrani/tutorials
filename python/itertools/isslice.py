from itertools import *

print list(islice('ABCDEFG', 2))
# ['A', 'B']

print list(islice('ABCDEFG', 2,4))
# ['C', 'D']

print list(islice('ABCDEFG', 2,4,1))
# ['C', 'D']

print list(islice('ABCDEFG', 2,2,1))
# []

print list(islice('ABCDEFG', 2, None))
# ['C', 'D', 'E', 'F', 'G']

print list(islice('ABCDEFG', 0, None, 2))
# ['A', 'C', 'E', 'G']

for i in islice(count(), 0, 100, 5):
	print i
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95