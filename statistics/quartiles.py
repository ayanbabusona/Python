n=int(input())
l=[int(a) for a in input().split()]
l.sort()
if(n%2==0):
    m1=l[n//2]
    m2=l[n//2-1]
    m=(m1+m2)//2
else:
    m=l[n//2]
if(n%2==0):
    if((n//2)%2==0):
        q1=l[n//4]
        q2=l[n//4-1]
        q=(q1+q2)//2
    else:
        q=l[n//4]
    if((n+n//2)%2==0):
        a1=l[(n+n//2)//2]
        a2=l[(n+n//2)//2-1]
        a=(a1+a2)//2
    else:
        a=l[(n+n//2)//2]
else:
    if((n//2)%2==0):
        q1=l[n//4]
        q2=l[n//4-1]
        q=(q1+q2)//2
    else:
        q=l[n//4]
    if((n+n//2+1)%2==0):
        a1=l[(n+n//2)//2]
        a2=l[(n+n//2)//2+1]
        a=(a1+a2)//2
    else:
        a=l[(n+n//2)//2]
print(q)
print(m)
print(a)
