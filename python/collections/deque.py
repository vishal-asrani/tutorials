from collections import *

d = deque("ghi")
print d
# deque(['g', 'h', 'i'])

d.append('j')
d.appendleft('f')
print d
# deque(['f', 'g', 'h', 'i', 'j'])

d.pop()
print d
# deque(['f', 'g', 'h', 'i'])

d.popleft()
print d
# deque(['g', 'h', 'i'])

print d[0]
# g

print d[-1]
# i

print('h' in d)
# True

d.extend('jkl')
print d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.rotate(1)
print d
# deque(['l', 'g', 'h', 'i', 'j', 'k'])

d.rotate(-1)
print d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

print(deque(reversed(d)))
# deque(['l', 'k', 'j', 'i', 'h', 'g'])

print d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.append("abc")
print d
# deque(['g', 'h', 'i', 'j', 'k', 'l', 'abc'])

d.clear()
print d
# deque([])