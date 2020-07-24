def lcm(a,b):
    for i in range(1,b+1):
        if (a*i) % b==0:
            print("there least common multiple is",a*i)
            break
lcm(6,5)