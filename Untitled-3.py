def remove_duplicates(input_list):
    seen = {}
    for item in input_list:
        seen[item] = seen.get(item, 0) + 1
    
    result = [item for item in input_list if seen[item] == 1]
    return result

user_list_str = input("Enter a list of elements separated by spaces: ")
user_list = user_list_str.split()


filtered_list = remove_duplicates(user_list)
print("Original list:", user_list)
print("List with elements occurring more than once removed:", filtered_list)
# Example of how to make it easier to test with a predefined list
# test_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
# filtered_test_list = remove_duplicates(test_list)
# print("\nTest List:", test_list)
# print("Filtered Test List:", filtered_test_list)
def remove_duplicates(input_list):
    seen = {}
    for item in input_list:
        seen[item] = seen.get(item, 0) + 1
    
    result = [item for item in input_list if seen[item] == 1]
    return result

user_list_str = input("Enter a list of elements separated by spaces: ")
user_list = user_list_str.split()


filtered_list = remove_duplicates(user_list)
print("Original list:", user_list)
print("List with elements occurring more than once removed:", filtered_list)
