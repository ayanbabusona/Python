da,ma,ya=list(map(int,input().split()))
de,me,ye=list(map(int,input().split()))
if(ya==ye):
    if(ma<=me):
        if(da<=de):
            print(0)
        else:
            print((da-de)*15)
    else:
        print((ma-me)*500)
elif(ya<=ye):
    print(0)
else:
    print(10000)
