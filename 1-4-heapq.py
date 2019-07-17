# 1-4-heapq.py

'''
just a quick play with heapq and a look at the docs

The heap data structure is generally used to create a priority queue.
In Python this case be done using the "heapq" module.

a heap is an array for which heap[k] <= heap[2 * k+1]
and heap[k] <= heap[2*k+2] for all k, counting elements from 0.

The interesting property of a heap is that heap[0] is always the smallest element.

'''
import heapq

jim = [ 2, 5, -3, 55, 0, 22, -8, 7]

heapq.heapify(jim)

print("The heap is : ", end="")
print(list(jim))


'''
useful to picture the priorty q as a tournament (as per the docs).

                        1
                   2         3
            4         5   6     7


heapq has the following functions:

heapify(x) - change list x into a heap, in-place in linear time (i.e. O(n) )
i.e. the running time increases, in the worst case scenario linearly with the input size

heappush(heap, item) - pushes the value item onto the heap, maintaining the heap

'''
