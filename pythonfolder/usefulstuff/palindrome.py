q=input("please enter an integer: ")
s=str(q)
l=[]
for i in range(0,len(s)):
    l.append(s[i])
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
if l2 ==l:
    print("the number you typed is a palindrome")
else:
    print("the number you typed is not a palindrome")    