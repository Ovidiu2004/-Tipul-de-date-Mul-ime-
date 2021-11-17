import itertools
multimea={'A','B','C','D'}
for i in range(len(multimea)):
    submultime=itertools.combinations(multimea, i+1)
    print(set(submultime))