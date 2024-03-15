nums = [9,4,1,7]
k = 3

nums=sorted(nums)
start=0
end=k-1

minimum=100000
while end<len(nums):
  minimum= min(nums[end]-nums[start],minimum)
  start+=1
  end+=1

print(minimum)

#In this code the biggest eureka moment was to realise that as it is sorted the windows size the first l and last element the r will always be smallest and biggest number which means we dont need to know the numbers in between

