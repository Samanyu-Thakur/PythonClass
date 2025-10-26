def print_triangle(rows, num):
    i = 0 
    for i in range(1, rows + 1):
        for j in range(i):
            print(num * i, end=' ')
            i+= 1
        print()

rows = int(input("Enter the number of rows: "))
num = int(input("Enter the number for the table: "))


print_triangle(rows, num)
