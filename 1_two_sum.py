nums = [2,7,11,15]
target = 9
# Output: [0,1]
data={}

for i in range(len(nums)):
  if nums[i] not in data.keys():
    data[target-nums[i]]=i

  else:
    print([data[nums[i]], i])
    # return [data[nums[i]], i]
    