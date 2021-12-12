"""bubble sort - complexity O(n^2)"""
def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(0,i-1):
            if lst[j] > lst[j+1]:
                x = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = x
    return lst

"""insertion sort - the complexity of algorithm is o(n2)"""
def insertion_sort(lt):
    for i in range(1,len(lt)):
        for j in range(i,0,-1):
            if(lt[j] < lt[j-1]):
                lt[j] , lt[j - 1] = lt[j-1] , lt[j]

    return lt



"""binary sort - complexity O(n*log(n)) - so its efficient than bubble sort"""

def binary_insertion_sort(lst):

    ret_list = []
    for i in range(0,len(lst)):
        binary_insert_value(ret_list,lst[i])
    return ret_list


def binary_insert_value(lst,element):
    middle_element = len(lst)//2
    if middle_element == 0:
        if len(lst)==0:
            lst.append(element)
        if len(lst) ==1:
            if (lst[0] > element):
                lst[0],lst[1] = element,lst[0]

    else:
        if (element > lst[middle_element]):
            binary_insert_value(lst[middle_element:len(lst)-1], element)
        else:
            binary_insert_value(lst[0:middle_element], element)




""" quick sort will work on the principle of finding a pivot. an element whose left 
are lesser elements and whose right are greater elements. it will keep finding pivot till lower index is lesser than 
upper index. This is in place sorting of data. because it uses divide and conquer algorithms - 8 elemets can be sorted in 
3 step worst case so the complexity is O(logn)"""

def quick_sort(lst):
    lower = 0
    upper = len(lst)-1

    quick_sort_implementation(lst,lower,upper)
    print(lst)


def quick_sort_implementation(lst,lower,upper):
    if (lower < upper):

        pivot = quick_sort_partition(lst,lower,upper)
        quick_sort_implementation(lst, lower, pivot-1)
        quick_sort_implementation(lst, pivot+1, upper)

def quick_sort_partition(lst,lower,upper):
    i=lower-1
    j=lower

    while j <= upper-1:
        if (lst[j] < lst[upper]):
            i = i+1
            lst[i],lst[j] = lst[j],lst[i]
        j=j+1

    lst[i+1],lst[upper] = lst[upper],lst[i+1]

    # returning pivot
    return i+1


if __name__== "__main__":

    lst1 = [0,2,1,3,5,4,6]
    lst2 = [0, 2, 1, 3, 5, 4, 6]
    #for i in range(len(lst1)-1, 0, -1):
    #    print(i)
    print("lst1 before sort"+str(lst1))
    print("lst1 after bubble sort is" + str(bubble_sort(lst1)))
    print("lst1 after quick sort is" + str(quick_sort(lst1)))
    print("lst1 after insertion sort is" + str(insertion_sort(lst1)))

