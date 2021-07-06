import sys

T = int(input())
data = []

for _ in range(T):
    data.append(int(sys.stdin.readline()))

max = max(data)

ott = [1,2,4]

for i in range(3,max):
    ott.append(ott[i-1]+ott[i-2]+ott[i-3])

for i in range(T):
    print(ott[data[i]-1])