import matplotlib.pyplot as plt

x=[1,2,5,6,8]
y=[1,2,3,7,5]

plt.figure(figsize=(15,8),facecolor='green')
plt.text(x[0]+0.1,y[0]-0.1,f'({x[0]},{y[0]})')
plt.text(x[1]+0.1,y[1]-0.1,f'({x[1]},{y[1]})')
plt.text(x[2]+0.1,y[2]-0.1,f'({x[2]},{y[2]})')
plt.text(x[3]+0.1,y[3]-0.1,f'({x[3]},{y[3]})')
plt.text(x[4]+0.1,y[4]-0.1,f'({x[4]},{y[4]})')


plt.scatter(x,y,color='red')
plt.savefig('3.jpg')
plt.show()

