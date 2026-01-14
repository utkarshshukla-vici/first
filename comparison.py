a= int (input ("enter value of a"))
b= int (input ("enter value of b"))
if a==b:
    print ("they ate equal")
if a > b :
    print (" a is greater then b")
else:
    print ("b is greater than a")
c= int (input ("enter value of c"))
d= int (input ("enter value of d"))
e = int (input ("enter value of e"))
if (a>c & b>c):
    print (c, "is the smallest")
if  (b>a & c>a):
    print (a,"is smallest")
if(a>b & c>b):
    print (b,"is smallest")