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

prime_number(9) 