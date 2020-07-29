string1='''a b c d e f g h i j k l m n o p q r s t u v w x y z'''
list1=string1.split(" ")
list1.reverse()
string2=""
for i in list1:
    string2+=i
    string2+=" "
print(string2)