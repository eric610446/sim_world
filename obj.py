import random
import var

class life:
	age='1'
	max_age='10'
	x=0
	y=0

	def __init__(self, max_age, x, y):
		self.max_age=max_age
		self.x=x
		self.y=y

	def set_age(self, n):
		self.age=n

	def show_x(self):
		return self.x

	def show_y(self):
		return self.y

	def set_x(self, n):
		self.x=n

	def set_y(self, n):
		self.y=n

	def move(self, n):
		move_s='5'
		if self.x!=0:	
			move_s+='4'
		if self.y!=0:	
			move_s+='2'
		if self.x!=var.map_size-1:	
			move_s+='6'
		if self.y!=var.map_size-1:	
			move_s+='8'
		
		act=random.choice(move_s)

		if(act=='2'):
			self.y-=n
			
		elif(act=='4'):
			self.x-=n

		elif(act=='6'):
			self.x+=n
			
		elif(act=='8'):
			self.y+=n
				


