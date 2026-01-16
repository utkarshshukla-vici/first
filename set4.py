b = {"megatron", "optimus", "bumblebee"}
print (b)
b.add("somkescreen")
print (b)
b.remove ("megatron")
print(b)
b.discard ("smokescreen")
print (b)
b.pop()
print (b)
c = {"rc","rachit", "bulkhead"}
print (b.union(c))
print (b.intersection(c))
d = {"rc"}
print (c.difference(d))