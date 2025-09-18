# print all primes before n using flag 
n = int(input("Enter no:- " ))
for num in range(2, n):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)
