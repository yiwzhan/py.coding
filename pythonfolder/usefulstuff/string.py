# stng="this is a string.... wow!"

# def mysplit(inputstring,seperator=" "):
#     lis=[]
#     um=0
#     for i in range(1,len(inputstring)):
#         m=inputstring[i-1]
#         if m== seperator:
#             lis.append(inputstring[um+len(seperator):i-1])
#             um=i-1 
#     lis.append(inputstring[um+1:len(inputstring)])
#     for c in range(1,len(lis)):
#         con=lis[c-1]
#         if con=="":
#             del lis[c-1]  
#     return lis

# teststring = "this is a     df    ;;j"    
# print(mysplit(teststring))

# def mysplit(inputstring,seperator=" "):
#     lis=[]
#     um=0
#     for i in range(1,len(inputstring)):
#         um=i-1
#         m=inputstring[um]
#         if m == seperator:
#             for l in range(1,um):
#                 del lis[0]
#         else:
#             lis.append(inputstring[0:len(inputstring)])
# teststring = "this is a     df    ;;j"    
# print(mysplit(teststring))
def mysplit(string1,seperator=" "):
    word=""
    mylist = []
    string1=string1+seperator
    for i in string1:
        if i!=seperator:
            word=word+i
        else:
            if word!="":
                mylist.append(word)
            print(word)
            word=""
    return mylist
s="hi      pop    corn"
print(mysplit(s))