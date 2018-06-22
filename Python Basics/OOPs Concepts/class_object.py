class Sparrow:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #instance method
    def eats(self,food):
    	return "{} eats {}".format(self.name,food)

# instantiate the Parrot class
fanny = Sparrow("Fanny", 5)
dora = Sparrow("Dora", 8)

# access the class attributes
print("Fanny is a {}".format(fanny.__class__.species))
print("Dora is also a {}".format(dora.__class__.species))

# access the instance attributes
print("{} is {} years old".format( fanny.name, fanny.age))
print("{} is {} years old".format( dora.name, dora.age))

print(fanny.eats("peanuts"))
print(dora.eats("rice"))