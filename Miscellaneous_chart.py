import matplotlib.pyplot as plt
x=[1,2,3]
h=[3,2,1]
fig,ax=plt.subplots(2,2)
ax[0][1].bar(h,x,color='y')
ax[0][0].pie(x)
ax[1][1].barh(x,h,color='r')
y=[]
for i in range(41):
  y.append(-(i-20)**2)
ax[1][0].plot(y,ls="--",lw=3,color="#6199f2")
ax[1][0].grid(alpha=0.2,ls=':')
plt.show()