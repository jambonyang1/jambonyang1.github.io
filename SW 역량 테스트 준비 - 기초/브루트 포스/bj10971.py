from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))

perms = permutations(range(N))

def main(N,data,perms):
    result = sys.maxsize

    for perm in perms:
        if data[perm[-1]][perm[0]]==0:
            continue
        sum = 0
        flag = True
        for i in range(N-1):
            st = perm[i]
            ed = perm[i+1]
            if data[st][ed]==0:
                flag = False
                break
            sum += data[st][ed]
            if sum >= result:
                flag = False
                break
        if not flag:
            continue
        sum += data[perm[-1]][perm[0]]
        result = min(sum,result)

    print(result)

main(N,data,perms)