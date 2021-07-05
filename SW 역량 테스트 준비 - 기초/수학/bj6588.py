def primeodd(a,b):
    if a%2==0 or b%2==0:
        return False
    for i in range(2,int(a**(0.5)+1)):
        if a%i == 0:
            return False
    for i in range(2,int(b**(0.5)+1)):
        if b%i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0: break
    for i in range(3,n//2+1):
        if primeodd(i,n-i):
            print(n," = ",i," + ",n-i)
            break
        else:
            if i == n//2+1:
                "Goldbach's conjecture is wrong."