for _ in range(int(input())):
	n,m=list(map(int,input().split()))
	s="*"
	x="."
	for i in range(n):
		for j in range(m):
			if i%2==0:
				if j%2==0:
					print(s,end="")
				else:
					print(x,end="")
			else:
				if j%2==0:
					print(x,end="")
				else:
					print(s,end="")
		print()