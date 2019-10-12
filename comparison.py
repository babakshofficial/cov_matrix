
# created by: Babak Shahriari
# comparing size and each value of the two matries
# peak is modified because of rounding around floating point
def comparison(listA, listB, peak):
    # whole length comparison
    if len(listA) != len(listB):
        return 0
    # each inner list length comparison
    for i in range(len(listA)):
        for j in range(len(listB)):
            if len(listA[i]) != len(listB[j]):
                return 0
    # each value length comparison rounded around floating point by a peak
    for i in range(len(listA)):
        for j in range(len(listB)):
            if round(listA[i][j],peak) != round(listB[i][j],peak):
                return 0
    return 1