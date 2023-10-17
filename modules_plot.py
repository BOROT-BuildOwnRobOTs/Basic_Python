import matplotlib.pyplot as plt

# x = ['Mon', 'Tue', 'Wed', 'Thru', 'Fri']
# y = [10, 20, 25, 30, 15]
# plt.bar(x, y, color='g', alpha=0.3)
# plt.show()

x = [1,2,3,4,5,6,7]
y = [32,45,87,23,6,87,23]
plt.plot(x,y, color='green', linestyle='-', marker='o', linewidth=1, markersize=7)
plt.title('simple line Graph')
plt.legend('L')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


