'''
1.1: Unpacking a sequence into separate variables

Problem: You have an n-element tuple or squence that we'd like to unpack into a
         collection of N variables

Solution: any sequence, or iterable can be unpacked into variables using simple assign.
          Only require that the number of vars & structure match the sequence
'''

p = (4, 5)

x,y = p

# print(x)
# print(y)

data = ['ACME', 50, 91.1, (2019, 6, 30) ]

company, age, iq, dob = data

# print(iq)

# can break it down even further
company, age, iq, (yr, mth, d) = data

# print(yr)

'''
such unpacking works with any object that happens to be iterable, not just tuples or
lists.  This includes strings, files, iterators & generators.
'''
s = "Hello"

a, b, c, d, e = s
print(a, c, e)

# to discard certain values, just use a throwaway variable e.g. _
_, a, b, c, _ = s

print(a, b, c)
