#keys and values method
d = {'first':'myfirst', 'second':[1,2,3]}
print d.keys()
print d.values()

#access to a value by key
print d['first']
print d.get('first')

#query info
print d.items()

#check if a key is present
print d.has_key('second')

#pop and popitem
print d.pop('first')
print d.popitem()
print d

d = {'first':'myfirst', 'second':[1,2,3]}
#create new object
t = d.copy()

#clear dictionary
t.clear()
print t

#create new item with a default value
t.setdefault('third','')
print t['third']

#create dictionary from a set of keys
print {}.fromkeys(['a','b'])

#update method 
a = {'x':1}
b = {'x':3,'y':4}
a.update(b)
print a['x']
print a['y']

#using iterators over values,keys or items
print [x for x in t.itervalues()]
print [x for x in t.iterkeys()]
print [x for x in t.iteritems()]
