flowerbed = [1,0,0,0,0,1]

n = 2
# Output: true
chances=list()
can_plant=True

for i in range(len(flowerbed)):
  
  if flowerbed[i]==1:
    can_plant=False
    if chances:
      chances.pop()
      chances.append(can_plant)
    
    chances.append(can_plant)

  elif flowerbed[i]==0 and can_plant==False:
    chances.append(False)
    can_plant=True

  else:
    chances.append(can_plant)


for x in range(len(chances)):
  if chances[x]==True:
    n-=1
    chances[x]=False
    if x<=len(chances)-1:
      chances[x+1]=False
    print(chances)

  if n==0:
    print('True')
    # return True
    


if n>0:
  print('False')
  # return False

# if chances.count(True) >= n:
#   print(True)
#   # return True
# else:
#   print(False)
#   # return False

# print(chances)
  # Here we most importantly learnt about list.count(element) as we could able to find the occurances of True element in the list
    