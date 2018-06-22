#append and extend method
l = ['a','b','c']
l.append(['d','e','f'])
print l

l = ['a','b','c']
l.extend(['d','e','f'])
print l

#find index in list
print l.index('c')

#insert in a list
l.insert(3,'m')
print l

#remove a single element from list
l.remove('m')
print l

#pop top element from list
l.pop()
print l

#find no of items in list
print l.count('a')

#reverse method
l.reverse()
print l

#sort method 
l.sort()
print l

#sort in reverse order
l.sort(reverse=True)
print l

#use of + and * operator
l=[1]
l += [2]
print l

l = l * 2
print l

#Slicing
x=[1,2,3,4,5,6,7,8,9,10]
print x[:]

print x[3:]

print x[4:-1]

print x[::]

print x[2::3]

#list comprehension
print [i for i in range(20) if i % 2 == 0]

#list as stack 
stack = ['a','b','c','d','e','f']
stack.append('g')
print stack
print stack.pop()
print stack

#list as queue 
queue = ['a','b','c','d','e','f']
queue.append('g')
print queue
print queue.pop(0)
print queue

#Copy a list using deepcopy
import copy
a = [4, 5, [8, 9]]
b = copy.deepcopy(a)
a[2][1] = 100
print a
print b