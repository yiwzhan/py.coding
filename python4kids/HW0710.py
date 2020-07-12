def prime_number(x):
    if x==1:
        print("it isnt prime or composite")
    else:    
        for i in range(2,x):
            if x % i==0:
                print("it isnt prime")
                break     
        else:
            print("it's a prime number")

prime_number(23)   

# def prime_number(x):
#     flag = 1   # if flag = 1, it's a prime number, if flag = 0, it's not a prime number

#     for i in range(2,x):
#         if x % i==0:
#             flag = 0
#             break     
        
#     if flag == 1:
#         print("it's a prime number")
#     elif flag == 0:
#         print("it's not a prime number")

# prime_number(1)   