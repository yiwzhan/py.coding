list1=[1,8,5,20,43,17,24,8,1,13,12,13]
target1=25
set1=set(list1)
list2=[]
for i in set1:
    s=target1-i
    if s in set1 and s not in list2:
        print(i,s)
        list2.append(i)

print(list2)

