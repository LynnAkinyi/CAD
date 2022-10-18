import matplotlib.pyplot as plt

y1 = [5000,10000,15000,20000,25000,30000,35000,40000]
x1 = [2.649,10.12,24.10,42.85,64.63,92.77,127.33,167.19]

plt.plot(x1,y1,label = "Line1")

y2 = [5000,10000,15000,20000,25000,30000,35000,40000]
x2 = [3.212,9.889,22.59,39.70,62.51,92.18,126.01,169.39]

plt.plot(x2,y2,label = "Line2")

plt.xlabel('x -axis')
plt.ylabel('y -axis')


plt.title('Graph of Array size against Time')
plt.show()

