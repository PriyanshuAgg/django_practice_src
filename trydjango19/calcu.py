for i in range(int(input())):
    n,k=input().split()
    n=int(n)
    k=int(k)
    count = 0
    sum = 0
    while(n!=0 or k!=0):
        sum =sum +((n%10+k%10)%10)*(10**count)
	    #print(sum)
        n= int(n/10)
        k = int(k/10)
        count += 1
    print(sum) 
