def insertionSort(list):
    # all the values after the first
    index_length = range(1, len(list))
    
    # to do an operation on all these values
    # for all the value is the index_length value,
    for i in index_length:

    # we want to sort those values
        sort = list[i]
       
        while list[i-1] > sort and i > 0:

            # swap
            list[i], list[i-1] = list[i-1], list[i]

            # to continue doing comparisons down the list,
            # look at the next item
            i = i - 1
 
    return list
 
print(insertionSort([7, 3, 4, 1, 9]))
