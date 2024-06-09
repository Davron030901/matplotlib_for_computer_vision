import matplotlib.pyplot as plt
x=[2,6,8,4,5]
y=[4,6,4,1,0]
for i in range(5):
  plt.text(x[i]+0.1,y[i]-0.1,f'({x[i]},{y[i]})')
plt.scatter(x,y,color='red')
plt.show()
