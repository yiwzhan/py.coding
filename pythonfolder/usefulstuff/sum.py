lis1=[]
def list_sum(list):
    sum = 0
    for i in list:
        u=int(i)
        sum = sum + u
    return sum

sum_result = list_sum(lis2)
print(sum_result)