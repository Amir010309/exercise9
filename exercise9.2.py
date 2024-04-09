t = int(input())
N = list(map(int,input().split()))
L = list(map(int,input().split()))
res1 = []
res2 = []

for i in range(len(N)):
    if len(N) <= 100000:
        res1.append(N[i])

for i in range (len(L)):
    if len(L) <= 100000:
        res2.append(L[i])

m = res1.union(res2)
print(len(m))
