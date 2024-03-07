nums1 = [4,1,2]
nums2 = [1,3,4,2]
# Output: [-1,3,-1]
result=[]
for i,x in enumerate(nums1):
  num_index= nums2.index(x)
  
  for j in nums2[num_index+1:]:
    
    if j>x:
      result.append(j)
      break
  if len(result)<i+1:
    result.append(-1)
  

print(result)