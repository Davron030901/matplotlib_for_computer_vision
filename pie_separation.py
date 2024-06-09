import matplotlib.pyplot as plt

x=[10,20,30]
labels=['A','B','C']
colors=['r','y','b']
explodes=[0.1,0.3,0]
plt.pie(x,labels=labels,colors=colors,explode=explodes)

plt.show()
