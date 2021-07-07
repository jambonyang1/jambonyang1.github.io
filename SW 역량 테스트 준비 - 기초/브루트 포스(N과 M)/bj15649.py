from itertools import permutations

N,M = map(int,input().split())
li = list(map(' '.join(permutations(map(str,range(1,N+1)),M))))
for i in li:
    print(i)
