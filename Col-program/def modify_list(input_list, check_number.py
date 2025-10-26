def modify_list(input_list, check_number, add_number):
    """
    Modifies a list by adding a specified number to each occurrence of another specified number.

    Args:
        input_list (list): The original list of numbers.
        check_number (int or float): The number to check for in the list.
        add_number (int or float): The number to add each time check_number is found.

    Returns:
        list: The modified list.
    """
    modified_list = []
    for item in input_list:
        if item == check_number:
            modified_list.append(item + add_number)
        else:
            modified_list.append(item)
    return modified_list

if __name__ == "__main__":
    try:
        user_list_str = input("Enter a list of numbers separated by spaces: ")
        user_list = [float(x) for x in user_list_str.split()]

        check_num = float(input("Enter the number to check for: "))
        add_num = float(input("Enter the number to add when the check number is found: "))

        result_list = modify_list(user_list, check_num, add_num)
        print("Original list:", user_list)
        print("Modified list:", result_list)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
            