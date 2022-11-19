#Lab1 Ex4
def harmonic(y):
    if y == 1 :
        value = 1
        return value
    else:
        value = 1/y+harmonic(y-1)
        return value

n = (int(input("Enter max value : ")))

for i in range(1,n+1):
    print("Limit =",i,", value =",harmonic(i))

