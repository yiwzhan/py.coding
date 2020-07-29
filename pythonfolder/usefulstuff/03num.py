lis1=[-25, -10, -7, -3, 2, 4, 8,-5, 10]
# lis1=sorted(lis1)
for i in range(1,len(lis1)):
    num1=lis1[i-1]
    for j in range(i+1,len(lis1)):
        num2=lis1[j-1]
        for k in range(j+1,len(lis1)):
            num3=lis1[k-1]
            if (num1+num2+num3)==0:
                print(num1,num2,num3,sep=", ")
