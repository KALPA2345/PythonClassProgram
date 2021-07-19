class student:

	def __init__(self,name,age,marks):

		self.name = name
		self.age = age
		self.marks = marks


	def talk(self):

		print("The name of student is {}\n, his age and marks are {}\n {} ".format(self.name,self.age,self.marks))


t1 = student("Durga",50,90)
t1.talk()
t2 = student("Ram",30,95)
t2.talk()























