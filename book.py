class book:
    def __init__ (self,name , price):
        self.name= name
        self.price = price

c1= book("time travel",100)
c2 = book ("a brief history of time", 250)
print (c1.name, c1.price)
print (c2.name, c2.price)