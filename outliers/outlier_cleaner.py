#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy as np
    from operator import itemgetter, attrgetter
    errors = abs(np.array(net_worths) - np.array(predictions))
    #errors = abs(net_worths - predictions)
    cleaned_data = zip(ages, net_worths, errors)
    print cleaned_data

    cleaned_data = sorted(cleaned_data,key=itemgetter(2))

    #cleaned_data = sorted(cleaned_data,key=itemgetter(2))
    limit = int(len(net_worths)*9/10)
    cleaned_data = cleaned_data[: limit]

    print list(cleaned_data)
    return cleaned_data


# import numpy as np
# from operator import itemgetter, attrgetter
# A = [3, 4, 6, 7]
# B = [1, 3, 6, 3]
# C = [1,2,3,4] 
# C2 = [1,2]
# D = A + B+ C2
# print list(np.array(A) - np.array(B))
# print zip(A, B,C)
# print len(zip(A, B,C))
# #sort_slit =  sorted(zip(A, B,C), key=itemgetter(1))

# print D
# print D[0:len(D)*9/10]
