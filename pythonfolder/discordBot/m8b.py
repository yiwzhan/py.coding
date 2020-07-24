import random
q=input("what is your question : ")
nm=random.randint(1,4)
m8b=["i dont know","yes","no","retry"]
if "magic 8 ball" in q:
    print(m8b[nm-1])
else:
    print("who are you talking too")