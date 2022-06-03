n, k = map(int, input().split())
ans = 0 
nums = [True] * (n + 1) 
for i in range(2, len(nums) + 1): 
    for j in range(i, n+1, i): 
        if nums[j] == True: 
            nums[j] = False 
            ans = ans + 1 
            if ans == k:
                print(j) 
                break
