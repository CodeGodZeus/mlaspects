n=int(input())    #T.Complexity==O(n**2)
nums=list(map(int,input().split()))
target=int(input())
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print(i,j)
            break
print(-1)
