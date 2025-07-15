n=int(input())
for i in range(n):
    ch=65+n-i-1
    for j in range(i+1):
        print(f"{chr(ch+j)}",end="")
    print()
