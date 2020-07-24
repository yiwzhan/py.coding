def multitable(x):
    for e in range(1,x+1):
        for i in range(1,e+1):
            print(i,'*',e,"=",i*e,end="  ")
        print("\n",end="")
multitable()
