class employee:
	def __init__(self):

		self.a = 'Durga'
		self.b = 10000
		self.c = 100

	def display(self):
		self.d = 500


e = employee()
e.display()

e.e = 700

print(e.__dict__)

