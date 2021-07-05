n = int(input())
data = list(map(int,input().split()))
count = 0

for _ in range(n):
    a = data[_]
    if a!=1:
        count += 1
        for i in range(2,int(a**(0.5)+1)):
            if a%i == 0:
                count -= 1
                break


print(count)