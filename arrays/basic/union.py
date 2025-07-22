def union(a,b):
    x=[]
    for i in range(len(a)):
        if a[i] not in x :
            x.append(a[i])
    for i in range(len(b)):
        if b[i] not in x :
            x.append(b[i])
    return x
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=union(a,b)
print(x)