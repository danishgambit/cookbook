'''
1-3. Keeping the last X items

Problem: We want to keep a limited history of the last few items seen during iteration or during
         some other kind of processing

Solution: Keeping a limited history is a perfect use of a collections.deque.
          e.g. the code below performs a simple text match on a sequence of lines & yields
          the matching line along with the previous N lines of context when found.
'''

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines

        previous_lines.append(line)


# using it
if __name__ == "__main__":
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)



'''
can use the maxlen argument to create a fixed-size queue.  If the queue is full and new
items are added, the oldest items is automatically removed
'''

q = deque(maxlen=4)
q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q)

q.append(5) # [2, 3, 4, 5]

'''
adding or popping items from either end of a queue has O(1) complexity.  This is unlike a list
where inserting or removing items from the front of the list is O(N).
'''
