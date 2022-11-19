#Lab1 Ex3
def primeFunction(num):
    n = num
    check = 1
    if n >= 1:
        Num = n
        if n > 1:  
            check = 0
            for x in range(2,n-1):
                if n % x == 0:
                    check = 1
                    break
        if check == 1:
            print(n, "is prime number")
        else:
            print(n, "is not prime number")
            
        primeFunction(Num-1)

primeFunction(int(input("Enter max  : ")))