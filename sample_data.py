import numpy as np
import matplotlib.pyplot as plot
import calculate_cov as COV
import comparison as COM

#initialization
N = 1000
mean = [0, 0]

#FIRST MATRIX
cov = [[1, 0], [0, 1]]

#multivariate_normal implementation includes cov
#normal Implementation includes standard Deviation
#produce N sample data based on multivariate normal (Gausian) distribution
sdata = np.random.multivariate_normal(mean, cov, N)

#converting class array type to simple list
#and disjoint columns
first_column = []
second_column = []
for i in range(N):
    first_column.append(sdata[:][i][0])
    second_column.append(sdata[:][i][1])

#plot.scatter(first_column, second_column)
plot.show()

#SECOND MATRIX
cov2 = [[1, 0.9], [0.9, 1]]
sdata2 = np.random.multivariate_normal(mean, cov2, N)

first_column2 = []
second_column2 = []
for i in range(N):
    first_column2.append(sdata2[:][i][0])
    second_column2.append(sdata2[:][i][1])
#plot.scatter(first_column2, second_column2)


#draw two scatter plots in a single figure
plot.figure('Scatter Plots')
plot.subplot(121)
plot.scatter(first_column, second_column)
plot.subplot(122)
plot.scatter(first_column2, second_column2)

#plot.show()

#comparison between numpy result and our simple way result
half = int(N/2)
print ("\nThe numpy Generated Values for: " + str(cov) + "\n")
result = np.cov(sdata)
print ("1. numpy[last][last] = " + str(result[-1][-1]))
print ("2. numpy[N/2][N/2] = " + str(result[half][half]))
print ("3. numpy[10][20] = " + str(result[10][20]))
print ("4. numpy[first][last] = " + str(result[0][-1]))
print ("5. numpy[last][first] = " + str(result[-1][0]))

print ("\nOur non-numpy Generated Values for: " + str(cov) + "\n")
non_numpy = COV.make_cov_matrix(sdata)
print ("1. non-numpy[last][last] = " + str(non_numpy[-1][-1]))
print ("2. non-numpy[N/2][N/2] = " + str(non_numpy[half][half]))
print ("3. non-numpy[10][20] = " + str(non_numpy[10][20]))
print ("4. non-numpy[first][last] = " + str(non_numpy[0][-1]))
print ("5. non-numpy[last][first] = " + str(non_numpy[-1][0]))
print (non_numpy == result)
print("\n**************************************************************************")
print ("\nThe numpy Generated Values for: " + str(cov2) + "\n")
result2 = np.cov(sdata2)
print ("1. numpy[last][last] = " + str(result2[-1][-1]))
print ("2. numpy[N/2][N/2] = " + str(result2[half][half]))
print ("3. numpy[10][20] = " + str(result2[10][20]))
print ("4. numpy[first][last] = " + str(result2[0][-1]))
print ("5. numpy[last][first] = " + str(result2[-1][0]))

print ("\nOur non-numpy Generated Values for: " + str(cov2) + "\n")
non_numpy2 = COV.make_cov_matrix(sdata2)
print ("1. non-numpy[last][last] = " + str(non_numpy2[-1][-1]))
print ("2. non-numpy[N/2][N/2] = " + str(non_numpy2[half][half]))
print ("3. non-numpy[10][20] = " + str(non_numpy2[10][20]))
print ("4. non-numpy[first][last] = " + str(non_numpy2[0][-1]))
print ("5. non-numpy[last][first] = " + str(non_numpy2[-1][0]))
print (non_numpy2 == result2)

#comparison Covariance Matrices by peak=10 of each value
print (COM.comparison(non_numpy,result,10))


