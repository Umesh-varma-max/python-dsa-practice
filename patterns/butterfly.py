'''
n=int(input())
s=2*(n-1)
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print(" "*s,end="")
    for j in range(i+1):
        print("*",end="")
    print() 
    s-=2
s+=4
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print(" "*s,end="")
    for j in range(n-i-1):
        print("*",end="")
    print() 
    s+=2
'''
n=int(input())
for i in range(n):
    st=i+1
    s=2*n-(2*(i+1))
    print("*"*st+" "*s+"*"*st)
s=2
for i in range(n-1,0,-1):
    st=i
    print("*"*st+" "*s+"*"*st)
    s+=2


