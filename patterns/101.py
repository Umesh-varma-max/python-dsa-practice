'''n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            if j%2==0:
                print(1,end="")
            else:
                print(0,end="")

        else:
            if j%2==0:
                print(0,end="")
            else:
                print(1,end="")
    print()'''
'''
n=int(input())
s=1
for i in range(n):
    if i%2==0:
        s=1
    else:
        s=0
    for j in range(i+1):
        print(s,end="")
        s=1-s
    print()'''


    


    