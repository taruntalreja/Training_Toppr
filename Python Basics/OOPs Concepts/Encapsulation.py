class Sparrow:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
    	self.__weight = 10
    	self.name = name
    	self.age = age
    
    #instance method
    def eats(self,food):
    	return "{} eats {}".format(self.name,food)

    def setWeight(self,weigh):
    	self.__weight=weigh

    def getWeight(self):
    	print("Weight : {}".format(self.__weight))

# instantiate the Parrot class
fanny = Sparrow("Fanny", 5)
fanny.getWeight()
fanny.__weight=100
fanny.getWeight()
fanny.setWeight(20)
fanny.getWeight()