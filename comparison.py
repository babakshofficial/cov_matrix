def comparison(listA, listB, peak):
    if len(listA) != len(listB):
        return 0
    for i in range(len(listA)):
        for j in range(len(listB)):
            if len(listA[i]) != len(listB[j]):
                return 0
    for i in range(len(listA)):
        for j in range(len(listB)):
            if round(listA[i][j],peak) != round(listB[i][j],peak):
                return 0
    return 1