arr = [17, 18, 5, 4, 6, 1]
# Output: [18, 6, 6, 6, 1, -1]

for i in range(len(arr) - 1):  # Adjust the range to stop at the second last index
    arr[i] = max(arr[i + 1:])

arr[-1] = -1  # Assign -1 to the last element separately
print(arr)


#I was getting some error because I was trying to access the last element of the array in the forloop and the max function was not able to handle that so smart move was to just add the -1 in the last element of the array