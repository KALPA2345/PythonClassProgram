
class student:

	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

	def talk(self):
		print("My name is ",self.name)
		print("my age is ",self.age)
		print("my marsks is",self.marks)

s = student('durga',49, 89)

s.talk()