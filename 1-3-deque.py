'''
quick play with the collections deque container

a list-like container with fast appends & pops on either end
'''
from collections import deque


d = deque('jim')

for let in d:
    print(let.upper())


d.append('bo')
d.appendleft('yo')

print(list(d)) # [ 'yo', 'j', 'i', ''m', 'bo']

d.pop() # remove right-most item - 'bo'
d.popleft() # remove left-most item - 'yo'

print(list(d))

print(d[0]) # first item

print(d[-1]) # right-most item

print(list(reversed(d))) # list contents in reverse

rev_d = reversed(d)

print(type(rev_d)) # deque ?

print('i' in d) # true
print('a' in d) # false

d.extend('xyz') # add multiple elements at onces

print(list(d))

d.rotate(1) # rotate 1 character right
print(list(d))

d.rotate(2)
print(list(d))

# let's put them back
d.rotate(-3) # rotate 1 character left

# empty the deque
d.clear()
# d.pop() # indexError

# extendleft reversesthe input order

d.extendleft('abc') # ['c', 'b', 'a']

'''
some common deque recipes from the documentation
'''

'''
bounded length deques give us functionality similar to tail in unix
'''
def tail(filename, n=2):
    'return the last n lines of a file'
    return deque(open(filename), 2)

jims_file = tail('somefile.txt', 2)

for line in jims_file:
        print(line, end='')

'''
Can use deques to maintain a sequence of recently added elements by appending to the right and popping to the left
'''
import itertools
def moving_average(iterable, n=3):
    # moving average ([40, 30, 50, 46, 39, 44]) --> 40.0, 42.0, 45.0, 43.0 ]
    it = iter(iterable)
    d = deque(itertools.islice( it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)

iq_list = [100, 130, 130, 130, 160, 145]

avg_iq = moving_average(iq_list)

for score in avg_iq:
    print(score)

'''
we can use the rotate(N) method to implement deque slicing & deletion.

'''
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = deque([x for x in range(1, 11)]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

delete_nth(d, 3) # i.e. delete the 4th element

print(d)
