add_factor=-9
for i in range(1,10000):
    num=i
    if add_factor==num-1:
        print(i-1,"is a perfect number")
    add_factor=0
    for d in range(1,num):
        if num % d ==0:
            add_factor+=d

