import matplotlib.pyplot as plt
plt.title("Parabola")
plt.xlabel("x",size=15,alpha=0.5)
plt.ylabel("y",size=15,alpha=0.5)

y=[]
plt.text(16,200,'y=x^2',size=20,alpha=0.5,style='italic')
for i in range(41):
  y.append((i-20)**2)
plt.plot(y,ls="--",lw=3,color="#6199f2")
plt.grid(alpha=0.2,ls=':')
plt.show()
'''import matplotlib.pyplot as plt
plt.title("Parabola")
plt.xlabel("x",size=15,alpha=0.5)
plt.ylabel("y",size=15,alpha=0.5)

y=[]
plt.text(16,200,'y=x^2',size=20,alpha=0.5,style='italic')
for i in range(41):
  y.append((i-20)**2)
plt.plot(y,ls="--",lw=3,color="#6199f2")
plt.grid(alpha=0.2,ls=':')
plt.show()'''