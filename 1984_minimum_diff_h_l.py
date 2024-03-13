nums = [9,4,1,7]
k = 2
# Output: 2
nums=sorted(nums)
if k==1:
  print(0)
l= 0
r=len(nums)-1

diff=1000000
while l<=r:
  diff = min(diff,nums[r]-nums[l])
  if diff

  