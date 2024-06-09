import matplotlib.pyplot as plt

x=[1,3,4,1]
y= [3,5,2,3]
x2=[3,4,2]
y2=[5,3,1]
plt.plot(x,y,color='r',linestyle=':',linewidth=5,marker='o',mec='b',mew=1,mfc='y',ms=18)

plt.plot(x2,y2,color='blue',alpha=0.4)
# xt=[]
# for i in range(10):
#   xt.append(0.5*i)
xt=([0,1,2,3,4])
plt.xticks([0,1,2,3,4],['A','B','C','D','E'])
plt.yticks(xt)
plt.show()


xt=[1,2,3,4,5,6]
xa=['A','B','C','D','E','F']
plt.xticks(xt,xa)