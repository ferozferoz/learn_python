
def print_spiral(lst):
    m=len(lst)

    for i in range(m):
        for j in range(i,m-i):
            print(lst[i][j])
            #print("printing i and j")
            #print(str(i)+""+str(j))
        #print('\n')
        #print('\n')

        for k in range(i+1, m-i):
            print(lst[k][j])
            #print("printing k and j"+str(i))
            #print(str(k) + "" + str(j))

        #print('\n')
        #print('\n')

        for l in reversed(range(i,m-i-1)):
            print(lst[k][l])
            #print("printing l and k")
            #print(str(k) + "" + str(l))
        #print('\n')
        #print('\n')

        for n in reversed(range(i+1,m-i-1)):
            print(lst[n][l])
            #print("printing n and l")
            #print(str(n) + "" + str(l))
        #print('\n')
        #print('\n')

if __name__=="__main__":
    """ Need to print this array in spiral order 
    1 2 3
    4 5 6
    7 8 9
    """
    lst = [[1,2,3],[4,5,6],[7,8,9]]
    lst1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12 ], [13, 14, 15, 16]]

    print_spiral(lst1)
