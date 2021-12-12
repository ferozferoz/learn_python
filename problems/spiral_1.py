def print_spiral(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)-i):
            print(lst[i][j])
        for k in range(i+1,len(lst)-i):
            print(lst[k][j])
        for l in reversed(range(i,len(lst)-i-1)):
            print(lst[k][l])
        for m in reversed(range(i+1,len(lst)-i-1)):
            print(lst[m][l])

if __name__=="__main__":
    """ Need to print this array in spiral order 
    1 2 3
    4 5 6
    7 8 9
    
    1 2 3 4
    5 6 7 8 
    9 10 11 12
    13 14 15 16
    """
    lst = [[1,2,3],[4,5,6],[7,8,9]]
    lst1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12 ], [13, 14, 15, 16]]

    print_spiral(lst)
