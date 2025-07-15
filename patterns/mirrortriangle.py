n=int(input())
s=2*(n-1)
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print(" "*s,end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    print()
    s=s-2
    