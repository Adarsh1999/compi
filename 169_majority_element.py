nums = [2,2,1,1,1,2,2]
# Output: 3

results={
}

for x in range(len(nums)):
  if nums[x] not in results.keys():
    results[nums[x]]=1
  else:
    results[nums[x]]+=1



for key, value in results.items():
    if value > len(nums)/2:
        print(key)
      # return key
        break
