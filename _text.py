import matplotlib.pyplot as plt
x=[3,1,-1]
y=[4,2,5]
plt.title('DATA',loc='right',pad=10,fontsize=20,color='#037ffc')

plt.text(1,3.5,
         'mohirdev',
         size=20,
         color='#837afc',
         weight=1000,
         style='italic')

plt.scatter(x,y)
plt.show()