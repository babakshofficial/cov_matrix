import numpy as np
import matplotlib.pyplot as plot
import calculate_cov as COV

N = 1000
mean = [0, 0]
cov = [[1, 0], [0, 1]]
sdata = np.random.multivariate_normal(mean, cov, N)

z = []
first_column = []
second_column = []
for i in range(N):
    first_column.append(sdata[:][i][0])
    second_column.append(sdata[:][i][1])

#plot.scatter(first_column, second_column)
plot.show()

cov2 = [[1, 0.9], [0.9, 1]]
sdata2 = np.random.multivariate_normal(mean, cov2, N)

first_column2 = []
second_column2 = []
for i in range(N):
    first_column2.append(sdata2[:][i][0])
    second_column2.append(sdata2[:][i][1])
#plot.scatter(first_column2, second_column2)

plot.figure('Scatter Plots')
plot.subplot(121)
plot.scatter(first_column, second_column)
plot.subplot(122)
plot.scatter(first_column2, second_column2)

plot.show()

print ("The numpy Generated Covariance Matrix \n")
result = np.cov(sdata2)
#print(result)
print ("\nOur non-numpy Generated Covariance Matrix \n")
non_numpy = COV.make_cov_matrix(sdata2)
#for i in range(len(non_numpy)):
#    print(non_numpy[i])
#print

