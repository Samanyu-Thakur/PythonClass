#     1
#   1  2
#  1  2  3
#   1  2
#    1
n = int(input("Enter no. of rows :- "))
for i in range(n):
    # Print spaces for centering
    print(" " * (n - i - 1), end="")
    # Print letters for this row
    for j in range(i + 1,0,-1):
        print(j + 1, end=" ")
        
    print()
for i in range(n-1, 0, -1): # n = 5 then i=4,3,2,1
    # Print spaces for centering
    print(" " * (n - i), end="") # n =5 i=4 then 5-4=1 space , i=3 then 5-3=2 spaces
    # Print letters for this row
    for j in range(i):
        print(j + 1, end=" ")
        
    print()