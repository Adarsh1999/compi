emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.


output=[]
for x in emails:
  x=x.split('@')
  x[0]=x[0].replace('.','')
  if '+' in x[0]:
    index=x[0].index('+')
    x[0]=x[0][:index]
  print(x)
  fullString=x[0]+'@'+x[1]
  if fullString not in output:
    output.append(fullString)

print(len(output))
# return len(output)