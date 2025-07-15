'''
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    ch="A"
    b=(2*i+1)//2
    for j in range(2*i+1):
        print(ch,end="")
        if j<b:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)
    for j in range(n-i-1):
        print(" ",end="")
    print()
'''
n = int(input())
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    ch = "A"
    b=(2*i+1)//2
    for j in range(2 * i + 1):
        print(ch, end="")
        if j<b:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)

    print()
