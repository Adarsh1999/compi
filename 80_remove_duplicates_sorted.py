nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

k=0
l=0
r=0
diff=0


while r<len(nums):

  if diff>2:
    to_delete.append()
  if nums[l]==nums[r]:
    diff+=1
    r+=1
  else:
    diff=0
    l=r
length=len(nums)
for x in to_delete:
  nums.remove(x)



print(nums)