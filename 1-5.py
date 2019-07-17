'''
1-5.py

Problem: We want to implement a queue that sorts items by a given priorty & always returns
         the item with the highest priority on each pop operation

Solution: Use the heapq module to implement a simple priority queue, as shown in the class below
'''

import heapq

class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self,item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

# use the class

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
        # return f"Item({self.name})"

# foo, bar have lowest priority, bar has highest followed by spam
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

q.pop() # Item('bar')
q.pop() # Item('spam')
q.pop() # Item('foo')
q.pop() # Item('grok')

'''
5 is the highest priority, so it's off first.
foo & grok both have the lowest priority, but notice that it returns in the same
order they were inserted into the queue
'''

'''
Discussion:  the core of this recipe uses the heapq module.  heapq.heappush() & heapq.heappop()
             insert & remove items from a list_queue such that the 1st item in the list has the
             smallest priority (see 1-4.py).  The heappop() method always returns the 'smallest' ite,
             so that's key for making the queue pop the correct items
'''
