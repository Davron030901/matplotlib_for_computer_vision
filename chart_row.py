import matplotlib.pyplot as plt

data={
    'Python':13.33,
    'C':11.41,
    'Java':10.33,
    'C#':7.04,
    'JavaScript':3.29,
    'Visual Basic':2.64,
    'SQL':1.53,
    'Assembly':1.34,
    'PHP':1.27
}
x=list(data.keys())
h=list(data.values())
plt.figure(figsize=(5,12))
plt.title('TIOBE Index for August 2023',fontsize=20)
plt.ylabel('Programming Languages',fontsize=15)
plt.xlabel('Rating',fontsize=15)
# print(x,h)
plt.barh(x,h,color="#6199f2")
plt.show()