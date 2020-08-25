n=int(input())
nums=list(map(int,input().split()))
target=int(input())
dict={}
for i in range(len(nums)):
    num=nums[i]
    complement=target-num
    if complement in dict:
        print(i,nums[complement])
    else:
        dict[nums]=i
print(-1)
     
