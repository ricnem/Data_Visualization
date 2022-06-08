import matplotlib.pyplot as plt


# A number raised to the third power is a cube.
# and then plot the first 5000 cubic numbers.
x_values = list(range(5001))
y_values = [x**3 for x in x_values]


# Make Plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)


# Set Chart and Label Axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


# Set size of tick labels, and set range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5000**3])


# Show plot
plt.show()
