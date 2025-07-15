n=int(input())
s=0
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print(" "*s,end="")
    for j in range(n-i):
        print("*",end="")
    print() 
    s+=2
s-=2
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print(" "*s,end="")
    for j in range(i+1):
        print("*",end="")
    print() 
    s-=2

'''
n = int(input())

# Upper Half
for i in range(n):
    stars = n - i
    spaces = 2 * i
    print("*" * stars + " " * spaces + "*" * stars)

# Lower Half
for i in range(n):
    stars = i + 1
    spaces = 2 * (n - i - 1)
    print("*" * stars + " " * spaces + "*" * stars)
'''
    
        
        
