# Plotting Pizza price against its diameter

# Training instance       Diameter (in inches)        Price (in dollars)
# 1                           		6                           7
# 2                           		8                           9
# 3                          	        10                          13
# 4                           		14                          17.5
# 5                           		18                          18

#Graphical representation of above table using matplotlib



import matplotlib.pyplot as plt

X=[[6],[8],[10],[14],[18]]
y = [[7], [9], [13], [17.5], [18]]
plt.figure()

plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')

plt.plot(X, y, 'k.')    #Remove 'k.' to see the best fit line
plt.axis([0, 25, 0, 25])
plt.grid(True)

plt.show()
