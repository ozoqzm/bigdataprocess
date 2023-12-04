import matplotlib.pyplot as plt

X = [ "Mon", "Tue", "Wed", "Thur", "Fri",  "Sat", "Sun" ]
Y = [-8, -5, -3, -4, -1, -10, -7]

plt.title("temperature per week")
plt.bar(X, Y, color='orange', width=0.3)
plt.xlabel("week")
plt.ylabel("temperature")
plt.show()

