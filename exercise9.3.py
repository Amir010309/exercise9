num = list(map (int,input().split()))
m = set()
for i in num:
    if i in m:
        
        print("Yes")
    else:
        print("No")
        m.add(i)