t=(1,2,3,4,2,5,2)
print t.count(2)
print t.index(5)

#tuples as key/value pairs to build dictionaries
d = dict([('first',1),('second',2),('third',3)])
print d['second']

#tuple unpacking
d = (4,5,6)
a,b,c = d
print a
print b

#tuple used as swap function
(a,b) = (b,a)
print a
print b

#length
print len(t)

#slicing
print t[4:]

#tuple to string
print str(t)

#Find maximum
print max(t)
