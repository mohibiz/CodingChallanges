def diagonalDifference(arr):
    left_list=[]
    right_list=[]
    for ind1, d1 in enumerate(arr):

        for ind2, d2 in enumerate(d1):
            if ind1==ind2:
                left_list.append(d2)
            if ind1+ind2==len(d1)-1:
                right_list.append(d2)
    return abs(sum(right_list)-sum(left_list))


if __name__ == '__main__':
    arr1= [[1,2,3],[4,5,6],[9,8,9]]
    arr2=[11, 2, 4],[4,5,6],[10, 8 ,-12]



    result = diagonalDifference(arr1)
    print(result)
    result = diagonalDifference(arr2)
    print(result)
