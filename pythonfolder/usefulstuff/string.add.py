st = "English = 78 Science = 83 Math = 68 History = 65"
def stringadd(str):
    txt = str.split(" ")       
    ls2=[]

    for i in txt:
        t=i.isnumeric()
        if t==True:
            ls2.append(int(i))
    sum=0   
    for m in ls2:
        sum+=m
    average = sum / len(ls2)
    print("the average is :", average)
    print('the sum is:' , sum)
stringadd(st)