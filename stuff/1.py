list1=[1,1,3,41,2,2,23.,13,1,23,1,3,12,3,1,2,31,2,3,35]
list2=[]
def clrnum(list):
    list.sort()
    hi=list[1]-1
    for i in list:
        if hi!=i:
            list2.append(i)
        hi=i        
    print(list2)
clrnum(list1)


