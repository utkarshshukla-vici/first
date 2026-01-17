class car:
    def __init__ (self,model,price):
        self.model = model
        self.price = price

c1= car("m4 sport",18000000)
c2 = car ("m2 coupe", 12000000)
print (c1.model, c1.price)
print (c2.model, c2.price)
