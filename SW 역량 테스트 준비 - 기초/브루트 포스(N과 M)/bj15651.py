from itertools import product

N,M = map(int,input().split())
li = map(str,range(1,N+1))
prod = list(product(li,repeat=M))
result = list(map(' '.join,prod))

print('\n'.join(result))