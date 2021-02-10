# class Myclass:
# 	raise_agee = 24
# 	def __init__(self,name,age,address):
# 		self.name = name
# 		self.age  = age
# 		self.address = address
# 		self.gmail = name+address+'@gmail.com' 
# 	def myfun(self):
# 		return '{}{}'.format(self.name,self.age)+'@gmail.com'
# 	def raise_age(self):
# 		self.age = self.age+self.raise_agee
# a1 = Myclass('sagar',25,'rentachintala')
# a2 = Myclass('rajesh',55,'hyd')
# a3 = Myclass('ramesh',67,'guntur')
# # print(a1.raise_age)
# # print(a1.myfun())
# # a1.raise_age()
# # print(a1.age)
# print(a1.__dict__ )


# class class1:
	
# 	def __init__(self):
# 		print('first')
# 	def myclass(self):
# 		print('second')
# 	def myclass1(self):
# 		print('third')
# class class2(class1):
# 	def __init__(self):
# 		super().__init__()
# 		print('one')
# a = class2()
# print(a.myclass())
# print(a.myclass1())
####################################
def Myclass(fun):
	def myfun():
		print('this is first')
		fun()
		print('this is third')
	return myfun
@Myclass
def Myclass1():
	print('this is second')
# Myclass1 = Myclass(Myclass1)
Myclass1()

