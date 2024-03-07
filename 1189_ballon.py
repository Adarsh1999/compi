text = "balon"
# Output: 2

from collections import Counter

final='balloon'
count=0
final_dict= Counter(final)
text_dic= Counter(text)

for i in final:
  if not text_dic[i]:
    print('0')
    # return 0
do_continue = True
while do_continue:
  for k,v in final_dict.items():
    print(k)
    text_dic[k]= text_dic[k]-final_dict[k]
    print(text_dic[k])
    if text_dic[k] <0 :
      do_continue=False
      break
      
  if do_continue:
    count+=1


print(count)