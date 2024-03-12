gain = [-5,1,5,0,-7]
# Output: 1
high=0
curr=0

for i in gain:
  curr+=i
  high=max(curr,high)

print(high)