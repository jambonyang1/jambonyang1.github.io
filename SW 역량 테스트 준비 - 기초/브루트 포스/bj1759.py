from itertools import combinations

L,C = map(int,input().split())
alphabet = sorted(list(input().split()))

combs = list(combinations(alphabet,L))

for comb in combs:
    count = 0
    for c in comb:
        if c in "aeiou":
            count += 1
    if count>0 and count<=L-2:
        print(''.join(comb))