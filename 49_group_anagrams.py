strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

output = defaultdict(list)
return_list = []

# Check if the input list contains only empty strings
if all(x == "" for x in strs):
    print([[""] * len(strs)]) 

for x in strs:
    # Sorting the string to identify anagrams
    sorted_x = ''.join(sorted(x))
    output[sorted_x].append(x)

for group in output.values():
    return_list.append(group)

print(return_list)

#Bhai sahhab the defauldict is god tier shit behenchod vo chiz ne automatically bana diya or check kar liya exist karta hai ki nhi bc sab handle kar diya 

# if x in output.keys():
#     output[x].append(strs[i])
# elif x not in output.keys():
#     output[x]=list()
#     output[x].append(strs[i])
#bC ye pura code defaul se hogaya
