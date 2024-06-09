import matplotlib.pyplot as plt
x=[8,7,6,5,2,1]
y=[5,2,7,3,2,1]
color=["b",(239/255, 145/255, 45/255),'g',"r",(227/255, 120/255, 224/255),(86/255, 6/255, 98/255)]
marker=[".","*","s","v","3","1"]
size=[50,80,300,200,80,100]
for i in range(6):
  plt.scatter(x[i],y[i],size[i],color[i],marker[i])
plt.show()