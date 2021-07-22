class student:

	def __init__(self, x, y, z):

		self.name = x
		self.age = y
		self.prof = z

	def display(self):

		print('The candidate name is {}, age {}, and prof {}'.format(self.name,self.age, self.prof))


t = student('Durga',40, 'Teaching')
t.display()

t = student('sunny','34','Dance')
t.display()
