""" IN THIS PROBLEM there will be array of 1 and 0 and you have to find out
continous 1 in the 2 d space. it could be vertical and horizontal continuity

0 1 0 0 0
1 1 1 0 0
0 1 0 0 1
0 0 0 0 1

for example here are two
"""


def count_island(grid):

    count = 0
    prev_row = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0

    }

    for row in grid:
        prev_element = 0
        i = 0
        for element in row:
            if element == 1 and prev_element == 0 and prev_row[i] == 0:
                count = count + 1
            if element == 1 and prev_element == 1 and prev_row[i] == 1:
                count = count - 1
            prev_element = element
            prev_row[i] = element
            i += 1
    return count


if __name__=="__main__":

    sea = [[1,1,1,1,0],
           [1,0,1,0,0],
           [1,0,0,0,1],
           [0,0,0,1,1]]

    sea1 = [[0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]

    print(count_island(sea))
    print(count_island(sea1))