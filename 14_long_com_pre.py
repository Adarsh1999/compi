strs = ["flower","flow","flight"]
long = strs[0]
for x in strs:
    for i in range(len(long)):
        if i == len(x) or x[i] != long[i]:
            long = long[:i]
            break
print(long)


# strs = ["flower", "flow", "flight"]
# longest_prefix = strs[0]

# for string in strs[1:]:
#     i = 0
#     while i < len(longest_prefix) and i < len(string) and longest_prefix[i] == string[i]:
#         i += 1
#     longest_prefix = longest_prefix[:i]

# print(longest_prefix)


#THese both are perfect answers of what I was thinking I missed the case in the while loop and like if the long is bigger than the string I saw the constraints which show that n2 is gonna work so I used 2 loops and realised how I can work