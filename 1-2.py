'''
1.2: Unpacking elements from iterables of Arbitrary Length

Problem: You need to unpack N elements from an iterable, but the iterable may be longer
         than N elements, cuasing a 'too many values to unpack' exception

Solution: star expressions - will address this problem.
          e.g. running a course & decide to decide at end of the term that we're going
          to drop the 1st & last homework grades, and only average the rest of them.
          Easy to do manually if there's only 4 homeworks but what if there's 24 ?
'''

from statistics import mean

def avg(inp_list):
    return sum(inp_list) / len(inp_list)

# use the mean method from the statistics module
def avg_alt(inp_list):
    return mean(inp_list)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg_alt(middle)

# another use case
# e.g. a user record with a name, email address then abritrary number of phone numbers
record = ('Jim', 'jim@example.com', '773-555-1212', '414-144-1144')

name, email, *phone_numbers = record

print(name)
print(phone_numbers)
# phone_numbers will always be a list, even if empty

'''
extended iterable unpacking is tailor-made for unpacking iterables of unknown or arbitrary length.
Often, these iterables have some unknown component or pattern in their construction (e.g. everything after
element 1 is a phone number) & star unpacking lets the developer leverage those patterns easily instead of
jumping thru' hoops to get at the relevant elements in the iterable.

the star syntax is especially useful when iterating over a sequence of tuples of varying length.
e.g. a sequence of tagged tuples
'''

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)

''' star unpacking can also be useful with certain kinds of string processing such as splitting
'''

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(":")
print(uname) # nobody
print(fields) # [ "*", "-2", "-2", "Unprivileged User" ]
print(homedir) # /var/empty
print(sh) # /usr/bin/false


'''
split the following list items into a head & tail components
[ 1, 10, 5, 2, 6, 2]
'''
items = [ 1, 10, 5, 2, 6, 2]

head, *tail = items
print(head)
print(tail)
