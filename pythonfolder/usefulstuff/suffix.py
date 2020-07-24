# filname=input("enter file name: ")
filename = "abc.text"
lastdotpos = filename.rfind(".")
print(filename[lastdotpos+1:len(filename)])




# filist=[]
# for i in range(1,len(filname)+1):
#     filist.append(filname[i-1])
# p=len(filist)*-1
# for u in range(-1,p-1,-1):
#     if filist[u]=='.':
#         for pe in range(u+1,0,-1):
#             print(filist[pe])
            
