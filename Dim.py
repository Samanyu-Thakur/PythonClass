def print_diamond(rows, num):
    """Prints a diamond pattern of a multiplication table."""
    # Print the upper part of the diamond (including the center row)
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        print(" " * (rows - i), end="")
        # Print the multiples for the current row
        for j in range(1, i + 1):
            print(num * j, end=' ')
        print()

    # Print the lower part of the diamond
    for i in range(rows - 1, 0, -1):
        # Print leading spaces for alignment
        print(" " * (rows - i), end="")
        # Print the multiples for the current row
        for j in range(1, i + 1):
            print(num * j, end=' ')
        print()


rows = int(input("Enter the number of rows for the half-diamond: "))
num = int(input("Enter the number for the table: "))


print_diamond(rows, num)
