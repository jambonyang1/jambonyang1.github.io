from itertools import permutations

N = int(input())
data = list(map(int,input().split()))
permute = list(permutations(data))

def diff(a):
    sum = 0
    for i in range(N-1):
        sum += abs(a[i]-a[i+1])
    return sum

maximum = 0
for i in range(len(permute)):
    maximum = max(maximum,diff(permute[i]))

print(maximum)