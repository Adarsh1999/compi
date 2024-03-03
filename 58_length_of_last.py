s = "   fly me   to   the moon  "
# Output: 4

s=s.strip()
print(s)
s=list(s)
count=0
for i in range(len(s)-1,-1,-1):
  
  if s[i]==" ":
    break
  count+=1

print(count)

