a,b,c = map(int,input().split())

a -= 1
b -= 1
c -= 1

result = b


while True:
    if result%15==a and result%19==c:
        break
    result += 28

print(result+1)
