def print_triangle(rows, num):
     
    for i in range(1, rows + 1):
        for j in range(1,i+1):
            print(num * j, end=' ')
           
        print()


rows = int(input("Enter the number of rows: "))
num = int(input("Enter the number for the table: "))


print_triangle(rows, num)
