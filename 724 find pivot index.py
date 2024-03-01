nums = [1,7,3,6,5,6]
# output=3

total=0
l=0
r=0

for x in nums:
  total+=x

for i in range(len(nums)):
  r= total-l-nums[i]
  if r==l:
   print(i)

  l=l+nums[i]

print(-1)