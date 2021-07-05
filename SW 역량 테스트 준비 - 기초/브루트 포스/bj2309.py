data = []
for i in range(9):
    data.append(int(input()))

sum = sum(data)
be = False
data.sort()
def printSeven(i,j):
    for a in range(9):
        if a!=i and a!=j:
            print(data[a])

for i in range(8):
    for j in range(1,9-i):
        if sum-data[i]-data[i+j]==100:
            printSeven(i,i+j)
            be = True
            break
    if be:
        break
