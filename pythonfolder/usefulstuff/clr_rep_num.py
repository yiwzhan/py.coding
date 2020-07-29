list1=[1,1,3,4,13,1,23,1,3,12,3,1,2,31,2,3,35]

def clrnum(list1):
    list2 = []
    # list.sort()
    # hi=list[1]-1
    for i in list1:
        if i not in list2:
            list2.append(i)       
    return list2

print(clrnum(list1))



