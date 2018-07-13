from collections import *

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print p
# Point(x=11, y=22)

print p[0] + p[1]
# 33

print p.x + p.y
# 33

t = [10, 20]
q = Point._make(t)
print q
# Point(x=10, y=20)

r = Point(x=11, y=22)
print r._asdict()
# OrderedDict([('x', 11), ('y', 22)])

print r
# Point(x=11, y=22)

print r._replace(x=33)
# Point(x=33, y=22)

print getattr(p, 'x')
# 11

print p._fields
# ('x', 'y')

Status = namedtuple('Status', 'open pending closed')._make(range(3))
print Status.open, Status.pending, Status.closed
# 0 1 2
