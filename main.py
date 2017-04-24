a = [1,2,3]
b = [2,3,10,11]

print "union"
print [x for x in a] + [x for x in b if x not in a]

print "intersection"
print [x for x in a if x in b]

print "set diff"
print [x for x in a if x not in b]

print "symmetric diff"
print [x for x in a if x not in b] + [x for x in b if x not in a]

print "caresian product"
print [(x,y) for x in a for y in ["red","blue"]]

