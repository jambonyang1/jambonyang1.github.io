from itertools import permutations
import sys

N = int(input())
data = list(map(int,input().split()))
ops_num = list(map(int,input().split()))
ops = ["+","-","*","/"]
arithmetic_ops = []
for i in range(4):
    operation = ops[i]
    temp = [operation]*ops_num[i]
    arithmetic_ops.extend(temp)

permute = list(set(permutations(arithmetic_ops)))

maximum = -sys.maxsize
minimum = sys.maxsize

for i in range(len(permute)):
    result = data[0]
    for j in range(N-1):
        if permute[i][j]=="+":
            result += data[j+1]
        elif permute[i][j]=="-":
            result -= data[j+1]
        elif permute[i][j]=="*":
            result *= data[j+1]
        elif permute[i][j]=="/":
            if result<0:
                result = -((-result)//data[j+1])
            else:
                result = result//data[j+1]
    maximum = max(maximum,result)
    minimum = min(minimum,result)


print(maximum)
print(minimum)
