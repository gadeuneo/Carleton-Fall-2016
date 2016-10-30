x=[1,2,2]
y=[3,2,3]
def dot(x,y):
	total = 0
	for i in range(len(x)):
		total = total + x[i] * y[i]
	return total
	
print(dot(x,y))
