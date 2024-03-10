nums = [1,1,1,2,2,3,3,3,3,4]
k = 2
# Output: [1,2]

from collections import Counter


nums_count= Counter(nums)
results=nums_count.most_common()
output=[]
for i in range(k):
  output.append(results[i][0])


print(output)