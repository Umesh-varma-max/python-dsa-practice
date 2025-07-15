n=list(map(str,input().split()))
o=[]
e=[]
for i in range(len(n)):
    if int(n[i])%2==0:
        e.append(n[i])
    else:
        o.append(n[i])
s="".join(o)
m="".join(e)
print(int(m)-int(s))

