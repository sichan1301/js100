for i in range(int(input())):
    stack = []
    isVps = True
    for j in input():
        if j == "(":
            stack.append(j)
        else:
            if stack:   #len(stack)>0
                stack.pop()
            else:
                isVps = False
    if len(stack)>0:
        isVps = False

    print('YES' if isVps else 'NO')
