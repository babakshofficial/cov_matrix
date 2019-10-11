import numpy as np
import matplotlib.pyplot as plot

N = 10
mean = [0, 0]
cov = [[1, 0], [0, 1]]
sdata = np.random.multivariate_normal(mean, cov, N)

z = []
first_column = []
second_column = []
for i in range(N):
    first_column.append(sdata[:][i][0])
    second_column.append(sdata[:][i][1])
plot.scatter(first_column, second_column)
plot.show()

cov2 = [[1, 0], [0, 1]]
sdata2 = np.random.multivariate_normal(mean, cov2, N)

z2 = []
first_column2 = []
second_column2 = []
for i in range(N):
    first_column2.append(sdata2[:][i][0])
    second_column2.append(sdata2[:][i][1])
plot.scatter(first_column2, second_column2)

result = np.cov(sdata, sdata2)
print(result)