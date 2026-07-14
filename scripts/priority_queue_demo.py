# python scripts/priority_queue_demo.py

import heapq

queue = []

heapq.heappush(queue, 7)
heapq.heappush(queue, 2)
heapq.heappush(queue, 10)
heapq.heappush(queue, 1)
heapq.heappush(queue, 5)

print(queue)
print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))