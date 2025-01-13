t=int(input())
while(t):
    n=int(input())
    count=0
    arr=[]
    k=1
    j=2
    m=0
    while count<n:
        x=j%k
        p= j
        n= k+1
        p= p+1
        y=(p)%(n)
        if x<y and x==m:
            arr.append(j)
            count+=1
            k=k+1
            m=m+1
            j=j+1

    t = t-1
        
    print(arr)
        
