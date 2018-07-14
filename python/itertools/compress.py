from itertools import *

print(list(compress('ABCDEF', [1,0,1,0,1,1])))
# ['A', 'C', 'E', 'F']