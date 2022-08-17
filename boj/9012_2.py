import sys

def stack_push(stack,value):
    stack.append(value)

def stack_pop(stack):
    last = stack.pop()  
    return last

k = int(sys.stdin.readline())

for i in range(k):
    stack=[]
    ok = True
    s = sys.stdin.readline().strip()
    for j in range(len(s)):
        if s[j] =='(':
            stack_push(stack,'(')
        elif s[j] ==')':
            if len(stack) == 0:
                ok = False
                break
            last = stack_pop(stack)
            if last =='(':
                continue
    if len(stack) != 0:
        ok = False
    if ok:
        print('YES')    
    else:
        print('NO')
