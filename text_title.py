import matplotlib.pyplot as plt
x=[3,1,-1]
y=[4,2,5]
plt.title('DATA',loc='right',pad=10,fontsize=20,color='#037ffc')

plt.xlabel('x',color='red')
plt.ylabel('y',color='green')
plt.scatter(x,y)
plt.show()