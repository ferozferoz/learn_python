def solution(A):
    # write your code in Python 3.6
    number_hills = 0
    number_valleys = 0
    for index in range(0, len(A)):
        if index == 0:
            pass
        else:
            if A[index] > A[index - 1]:
                # also confirm if index-n is greater
                k = index - 1
                while A[k] == A[k - 1] and k > 0:
                    k = k - 1

                if k == 0:
                    number_valleys = number_valleys + 1
                else:
                    if A[k] < A[k - 1]:
                        number_valleys = number_valleys + 1

            if A[index] < A[index - 1]:

                k = index - 1
                while A[k] == A[k - 1] and k > 0:
                    k = k - 1

                if k == 0:
                    number_hills = number_hills + 1
                else:
                    if A[k] > A[k - 1]:
                        number_hills = number_hills + 1

            if A[index] == A[index - 1]:
                pass

    j = index
    while A[j] == A[j - 1] and j > 0:
        j = j - 1

    if A[j] < A[j - 1]:
        number_valleys = number_valleys + 1
    else:
        number_hills = number_hills + 1

    return number_hills + number_valleys

def solution_1(A):
    hills=0
    valleys=0
    new_A=[]
    prev_element = None
    for element in A:
        if element != prev_element:
            new_A.append(element)
        prev_element=element
    for i in range(len(new_A)):
        if i == 0:
            if new_A[i] > new_A[i+1]:
                hills = hills+1
            if new_A[i] < new_A[i+1]:
                valleys = valleys+1

        elif i==len(new_A)-1:
            if new_A[i] > new_A[i-1]:
                hills = hills+1
            if new_A[i] < new_A[i-1]:
                valleys = valleys+1
        else:
            if new_A[i] > new_A[i-1] and new_A[i] > new_A[i+1]:
                hills = hills + 1
            if new_A[i] < new_A[i-1] and new_A[i] < new_A[i+1]:
                valleys = valleys + 1
    return hills+valleys


if __name__ == "__main__":
    lst = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
    lst = [2,3,4,3,2,1,2,5]

    print(solution(lst))
