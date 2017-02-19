import numpy as np
import matplotlib.pyplot as plt

class spline():

	def __init__(self,k1,k2,x1,y1,x2,y2):
		self.k1 = k1
		self.k2 = k2
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def set_params(self,k1,k2,x1,y1,x2,y2):
		self.k1 = k1
		self.k2 = k2
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def calculate_spline(self,x):
		def t(x):
			return ((x-self.x1)/(self.x2-self.x1))
		def a(x):
			return self.k1*(self.x2-self.x1)-(self.y2-self.y1)
		def b(x):
			return -self.k2*(self.x2-self.x1)+(self.y2-self.y1)
		return (1-t(x))*self.y1 + t(x)*self.y2 + t(x)*(1-t(x))*(a(x)*(1-t(x))+b(x)*t(x))

	def plot_spline(self,f):
		start = self.x1
		end = self.x2
		step = .1
		t = np.arange(start, end, step)
		# red dashes, blue squares and green triangles
		plt.plot(t, f(t), 'r')
		plt.show()
		plt.close()

	def slope(self,x,dx):
		return (self.calculate_spline(x+dx)-self.calculate_spline(x))/dx

spline = spline(3,2,0,1,3,4)
spline.plot_spline(spline.calculate_spline)
print(spline.slope(0,.1))


