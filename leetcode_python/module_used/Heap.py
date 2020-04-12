"""
heapq -- provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
Heaps are binary trees for which every parent node has a value less than or equal to any of its children

heapq.heappush(heap, item)¶ Push the value item onto the heap, maintaining the heap invariant
"""
import heapq

"heap like priority queue, the minimum tree"
h = []      # make a list to store the heap
heapq.heappush(h, (5, 'write code'))        # put element into heap flowing the heap order
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
heapq.heappush(h, (5, 'create tests'))
print(h)

heapq.heappop(h)    # pop out the first element
print(h)

s = [1,3,4,2,5,9,1]
heap_s = heapq.heapify(s)       # heapq.heapify make the list heap in place
print(s, '\n', heap_s)