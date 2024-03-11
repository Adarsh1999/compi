s = "A man, a plan, a canal: Panama"
# Output: true
final=''
for x in s:
  if x.isalpha() or x.isnumeric():
    final+=x.lower()
print(final)
print(final == final[::-1])