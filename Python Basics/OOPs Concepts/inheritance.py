#base class
class Bird:
	def __init__(self):
		print("This is bird class")
	def whoIsThis(self):
		print("This is a bird")
	def fly(self):
		print("Bird flies faster")

#child class
class Ostrich(Bird):
	def __init__(self):
		super().__init__()
		print("This is Ostrich class")
	def whoIsThis(self):
		print("This is an Ostrich")
	def run(self):
		print("Ostrich runs faster")

ossie = Ostrich()
ossie.whoIsThis()
ossie.fly()
ossie.run()