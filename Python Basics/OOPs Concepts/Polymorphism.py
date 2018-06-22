#base class
class Sparrow:
	def fly(self):
		print("Sparrow flies faster")

#child class
class Ostrich:
	def fly(self):
		print("Ostrich cannot fly")

#common interface
def flyTest(bird):
	bird.fly()

ossie = Ostrich()
sparr = Sparrow()
flyTest(ossie)
flyTest(sparr)