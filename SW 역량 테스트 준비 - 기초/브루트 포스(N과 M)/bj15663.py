from itertools import permutations
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
li = list(map(str,input().split()))
prod = list(permutations(li,M))
prod = sorted(list(set(prod)))

for result in prod:
    print(*result)