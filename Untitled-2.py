# Take two lists as input from the user
list1 = input("Enter the first list (comma-separated): ").split(',')
list2 = input("Enter the second list (comma-separated): ").split(',')
 
# Determine the length of the shorter list for zipping
min_len = min(len(list1), len(list2))
 
# Combine elements up to the length of the shorter list
result = [list1[i] + list2[i] for i in range(min_len)]
 
# Append the remaining elements from the longer list
result.extend(list1[min_len:])
result.extend(list2[min_len:])
 
# Print the final combined list
print("Result:", result)
