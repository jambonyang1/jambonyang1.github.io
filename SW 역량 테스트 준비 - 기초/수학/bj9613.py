n = int(input())

def gcd(a,b):
    while True:
        temp = a%b
        if temp==0:
            break
        else:
            a = b
            b= temp
    return b

for _ in range(n):
    data = list(map(int,input().split()))
    result = 0
    for i in range(1,data[0]):
        for j in range(1,data[0]-i+1):
            result += gcd(data[i],data[i+j])
    print(result)


