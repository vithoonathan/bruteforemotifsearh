import itertools as it

DNAStr = [ "actgaaggtcctctggctatccaggtacttacccctttggaactgtgcgaatctatgcgtttccaaccatgtctc",
           "agtactggtgtacatttgatccattgatgatagattagagcaacctgaaacaaacgctcagaaccagaagtgctt",
           "atcggtcgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatccttcggaatcta",
           "agtactggtgtacatttgatccattgatgatagattagagcaacctgaaacaaacgctcagaaccagaagtgctt"]

t,n,l=4,75,10  # No of strings, no of lines, set of string


def score(DNAStr, s):
    baseArr = ['a', 't', 'g', 'c']
    lis = []
    k = 0
    for d in DNAStr:
        tempArr = []
        for w in d[s[k]:s[k] + l]:
            tempArr.append(w)

        k += 1
        lis.append(tempArr)
    i = 0
    matArr = []

    i1 = 0
    while i1 < len(baseArr):
        j1 = 0
        arr1 = []
        while j1 < l:
            arr1.append(0)
            j1 += 1
        matArr.append(arr1)
        i1 += 1
    while i < len(baseArr):
        j = 0
        while j < l:
            k = 0
            while k < t:
                if baseArr[i] ==lis[k][j]:
                    matArr[i][j] += 1
                k += 1
            j += 1
        i += 1

        x = 0
        sum = 0
        while x < l:
            y = 0
            max = 0
            while y < len(matArr):
                if matArr[y][x] > max:
                    max = matArr[y][x]
                y += 1
            sum += max
            x += 1
    return sum



def bruteForceAlgo(DNAStr, t, n, l):
    data = it.product(range(n-l+1), repeat=t)
    bestScore = 0
    bestMotif = []
    for s in data:
        sco = score(DNAStr, s)
        if sco > bestScore:
            bestMotif = s
            bestScore = sco

    print("Best Score: ", bestScore)
    print("Best Motif: ", bestMotif)

    return bestMotif


bruteForceAlgo(DNAStr, t, n, l)
