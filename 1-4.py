'''
1.4.  Finding the largest or smallest N items

Problem: WE want to make a list of the largest or smallest N items in a collection.

Solution:  The heapq module has 2 functions nlargest() and nsmallest() that do exactly this.
'''

import heapq  # a.k.a. the priorty queue

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nsmallest(3, nums)) # prints [ -4, 1, 2]
print(heapq.nlargest(2, nums)) # prints [ 42, 37]

'''
both functions also accept a key parameter that means we can use them with more
complicated data structures.
'''
portfolio = [
    {'name' : 'IBM', 'shares' : 100, 'price' : 91.1},
    {'name' : 'AAPL', 'shares' : 50, 'price' : 543.22},
    {'name' : 'FB', 'shares' : 200, 'price' : 21.09},
    {'name' : 'HPQ', 'shares' : 35, 'price' : 31.75},
    {'name' : 'YHOO', 'shares' : 45, 'price' : 16.35},
    {'name' : 'ACME', 'shares' : 75, 'price' : 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])

print(expensive[0]['name'])

'''
cheap & expensive above are equivalent to the non-heapq phrases shown below.

nsmallest & nlargest perform best for smaller values of n.  For larger values, it's more efficient
to use the sorted() function.  When n==1, it's more efficient to use the built in min() & max()
functions.
'''
cheap2 = sorted(portfolio, key=lambda s: s['price'])[:3]
expensive2 = sorted(portfolio, key=lambda s: s['price'], reverse=True)[:1]

cheapest_one = min(portfolio, key=lambda s: s['price'])
priciest_one = max(portfolio, key=lambda s: s['price'])
