import heapq

list = []

heapq.heappush(list, 6)
heapq.heappush(list, 12)
heapq.heappush(list, 0)
heapq.heappush(list, -5)
heapq.heappush(list, 8)

print(list)

while list:
    print(list[0])
    heapq.heappop(list)