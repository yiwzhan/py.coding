def my_factorial(num):
    current_factorial = 1
    for i in range(1,num+1):
        current_factorial = current_factorial *i 
    return current_factorial
    
factorial=my_factorial(10)
print(factorial)