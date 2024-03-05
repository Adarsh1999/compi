nums = [0,1,2,2,3,0,4,2]   
val = 2
# Output: 2, nums = [2,2,_,_]
length=len(nums)
i=0
k=0
while i < len(nums):
  if nums[i] != val:
    i+=1
    
  else:
    k+=1
    nums.remove(nums[i])
    nums.append(-1)
    if i == 0:
      continue
    i-=1
    
k=length-k    

del nums[k:]
print(nums)

#Did it but the solution is definately not the best solution as this can be way shorter solution the better solution is pasted below":-


# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2

# k = 0  # This will keep track of the index to update
# for i in range(len(nums)):
#     if nums[i] != val:
#         nums[k] = nums[i]  # Move the element not equal to val to the front
#         k += 1  # Increment k to update the next index

# # After the loop, k represents the number of elements not equal to val
# # So, the first k elements in nums are the ones we want to keep
# # We can remove the remaining elements from nums
# del nums[k:]

# print(nums)
