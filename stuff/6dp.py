import random
passcode=[]
def g6dp():
    for i in range(1,7):
        chooser=random.randint(1,2)
        randnum=random.randint(1,9)
        if chooser==1:
            passcode.append(randnum)
        else:    
            letlist=["a","b","c","d","e","f","g","h","i"]
            passcode.append(letlist[randnum-1])
    print(passcode)        
g6dp()
            
    