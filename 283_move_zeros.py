nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

l=0
for r in range(len(nums)):
  if nums[r]:
    nums[l],nums[r]=nums[r],nums[l]
    l+=1


print(nums)

# so the whole logic worked like we want to shift non zeros into left side so here 2 pointers one is l which is remaining in left and other is r which will send non zeros towards left