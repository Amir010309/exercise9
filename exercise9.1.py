N = int(input())
list = list(map(int,input().split()))
res = []

for i in range(len(list)):
    res.append(list[i])
    
m = set(res)  

if list[i] > 20000000000:
    print ("end")
else:
    print ("Количество различных чисел:", len(m))