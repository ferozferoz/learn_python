""" IN THIS PROBLEM there will be array of 1 and 0 and you have to find out
continous 1 in the 2 d space. it could be vertical and horizontal continuity

0 0 0 0 0
0 1 1 0 0
0 1 0 0 1
0 0 0 0 1

for example here are two
"""

def find_island(lst):

    count_island = 0
    prev=0

    prev_lst = []
    for i in range(len(lst)):
        prev_lst.append(0)


    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == 0:
                if lst[i][j] == 1 and prev == 0 and prev_lst[j] == 0 and prev_lst[j+1] == 0:
                    count_island += 1
            elif j == len(lst[i])-1:

                if lst[i][j] == 1 and prev == 0 and prev_lst[j-1] == 0 and prev_lst[j] == 0:
                    count_island += 1
            else:
                if lst[i][j] == 1 and prev == 0 and prev_lst [j] == 0 and prev_lst[j+1] == 0 and prev_lst[j-1] == 0:
                    count_island += 1

            prev = lst[i][j]
        prev_lst = lst[i]
    return count_island


if __name__=="__main__":
    lst = [
        [0 ,1 ,0 ,0 ,1],
        [1 ,0 ,1 ,0 ,0],
        [0 ,1, 0 ,0 ,1],
        [0 ,0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]

    count_list = find_island(lst)
    print("count of islands" + str(count_list))