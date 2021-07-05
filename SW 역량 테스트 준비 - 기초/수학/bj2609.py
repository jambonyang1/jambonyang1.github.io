n,m = map(int,input().split())

d = n
while True:
    if d%m==0:
        break
    d+=n

while True:
    temp = n%m
    if temp==0:
        break
    else:
        n = m
        m = temp

print(d)
print(m)
