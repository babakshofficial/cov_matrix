# calculating Mean
def mean(x):
    return sum(x) / len(x)

#calculating covariance between the two same sized sets
def cov(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    data = [(x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))]
    return sum(data) / (len(data) - 1)

#creating covariance matrix
def make_cov_matrix(sdata):
    cov_matrix = []
    for i in range(len(sdata)):
        tmp = []
        for j in range(len(sdata)):
            tmp.append(cov(sdata[i],sdata[j]))
        cov_matrix.append(tmp)
    return cov_matrix
