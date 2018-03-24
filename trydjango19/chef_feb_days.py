for i in rnge(int(input())):
	n=int(input())
	c=[]
	d=[]
	m=list(map(int,input().split()))
	a=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
	for j in range(len(m)):
		if(m[j]!=0):
			c.append(m[j])
			d.append(a[j])
	print(c,d)