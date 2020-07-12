# def multitable(x):
#     for e in range(1,x+1):
#         for i in range(1,e+1):
#             if i==e:
#                 print(i,'*',e,"=",i*e)
#             elif i!=e:
#                 print(i,'*',e,"=",i*e,end="  ")
# multitable(8)

def multitable(x):
    for e in range(1,x+1):
        for i in range(1,e+1):
            print(i,'*',e,"=",i*e,end="  ")
        print("\n",end="")
multitable(3)

# def multitable(x):
#     for e in range(1,x+1):
#         for i in range(1,e+1):
#             print(i,'*',e,"=",i*e,end="  ")
#         print(" ")
# multitable(3) 