# HW 01. Write a Python function to find the Max of three numbers:

# def number_max(a,b,c):
#     a=int(a)
#     b=int(b)
#     c=int(c)
#     if a>b and a>c:
#         print( "a is the biggest")
#     elif b>a and b>c:
#         print( "b is the biggest")
#     elif c>a and c>b:
#         print("c is the biggest")
#     else:
#         print("there the same")   
# number_max(6,6,6)
# hj=[132,4,32,9,786,14,43]
# hi = [-12,-4,-8, -10]
# def list_max(list):
#     max_list=list[0]
#     for i in list:        
#         if max_list<i:
#             max_list=i
#     return max_list       
# x=list_max(hi)
# print(x)          

# lis1=[4,8,2]
# lis2=[4,8,2,4,5,6]
# def list_sum(list):
#     sum = 0
#     for i in list:
#         u=int(i)
#         sum = sum + u
#     return sum

# sum_result = list_sum(lis2)
# print(sum_result)


# lis1=[4,8,2]
# lis2=[4,8,2,4,5,6]
# def list_product(list):
#     product = 1
#     for i in list:
#         u=int(i)
#         product = product * u
#     return product

# product_result = list_product(lis1)
# print(product_result)


# def my_factorial(num):
#     current_factorial = 1
#     for i in range(1,num+1):
#         current_factorial = current_factorial *i 
#     return current_factorial
    
# factorial=my_factorial(10)
# print(factorial)

def prime_number(x):
    print(x)
    for i in range(2,x):
        print("x%i=",x%i)
        if x % i==0:
            print("it isnt prime")
            break     

prime_number(7)         