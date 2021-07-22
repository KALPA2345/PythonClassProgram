class test:
	def __init__(self):

		self.a = 'Durga'
		self.b = 10000
		self.c = 100
		self.d = 5

	def m1(self):
		del self.d


t = test()

print(t.__dict__)

t.m1()

print(t.__dict__)

del t.c

print(t.__dict__)
