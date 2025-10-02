def print_diamond(rows, num):
    

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
