import math
nums = [1,12,-5,-6,50,3]
k = 4
# Output: 12.75000

highest=-math.inf
l=0
r=0
curr=0
for i in range(len(nums)):
  if i>=k-1:
    r=i
    curr+=nums[r]
    highest=max(highest,curr)
    curr-=nums[l]
    l+=1
    
  else:
    r=i
    curr+=nums[i]

print(highest/k)