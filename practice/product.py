from itertools import product

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

print(list(product(iterable1,iterable2,iterable3)))


# iterable1 = 'ABCD'
# iterable2 = 'xy'
# iterable3 = '1234'

# for value1 in iterable1:
#   for value2 in iterable2:
#     for value3 in iterable3:
#       print(value1,value2,value3)