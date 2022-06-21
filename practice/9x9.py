# print([f' {i} x {j} = {i*j}' for i in range(2,10) for j in range(1,10)])

n = int(input())
def gugu(n):
  for i in range(1,n+1):
    print("\n")
    for j in range(1,10):
      print(f'{i}*{j}={i*j}',end='\t')

print(gugu(6))