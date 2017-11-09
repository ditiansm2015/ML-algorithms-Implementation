# Training instance       Diameter (in inches)        Price (in dollars)
# 1                           		6                           7
# 2                           		8                           9
# 3                          	        10                          13
# 4                           		14                          17.5
# 5                           		18                          18

#Linear Regression

#Estimating price of a 12" pizza using Linear Regression

from sklearn.linear_model import LinearRegression
# Training data
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
# Create and fit the model
model = LinearRegression()
model.fit(X, y)
print 'A 12" pizza should cost: $%.2f' % model.predict(12)
