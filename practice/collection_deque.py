from collections import deque

list = deque()

list.append(123)
list.append(456)
list.append(789)

print("size : ",len(list))
while len(list)>0:
    print(list.popleft())