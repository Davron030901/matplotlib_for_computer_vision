import matplotlib.pyplot as plt
x1=[3,1,-1]
y1=[4,2,5]

x2=[1,1.5,0]
y2=[3,6,2]

plt.scatter(x1,y1,label='circle')
plt.scatter(x2,y2,marker='s',label='square')
plt.legend(loc='lower right',ncol=2)#loc=6
plt.show()