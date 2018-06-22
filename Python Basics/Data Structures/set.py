a = set([1, 2, 3])
<<<<<<< HEAD
b = set([2, 3, 4])
=======
b = set([2, 3, 4, 5])
>>>>>>> a868250a314ce4f3c674386c39946139f998f1fa

#different methods on set

c = a.intersection(b)
print c

print c.issubset(a)
print c.issuperset(a)
print c >= a

print a.difference(b)
print a - b

print a.symmetric_difference(b)
print a^b

#copy a set
x = a.copy()
print x
