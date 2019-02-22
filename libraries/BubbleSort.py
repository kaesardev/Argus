'''
    BUBBLE SORT LIBRARY
'''
def bubbleSort(array):
    ''' Returns the ordered order list in order grows '''
    elements = len(array)-1
    ordered = False
    while not ordered:
        ordered = True
        for i in range(elements):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
                ordered = False 
    return array