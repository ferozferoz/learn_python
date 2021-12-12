# we will pass the list

"""selection sort - find the minimum element and place it in the beginning"""


def selection_sort(list_to_be_sort):
    if len(list_to_be_sort) == 1:
        return list_to_be_sort
    else:
        lesser = list_to_be_sort[0]
        for i in range(1, len(list_to_be_sort)):
            if list_to_be_sort[i] < lesser:
                lesser = list_to_be_sort[i]
        list_to_be_sort.remove(lesser)
        return [lesser] + selection_sort(list_to_be_sort)


"""quick sort basically is a recusive method of finding correct position of
pivot element in the list, working recursively the whole list is sorted in correct order"""


def quick_sort(lst):
    quick_sort_impl(lst, 0, len(lst) - 1)


def quick_sort_impl(lst, lower_index, upper_index):
    if lower_index < upper_index:
        pivot = find_pivot(lst, lower_index, upper_index)
        quick_sort_impl(lst, lower_index, pivot - 1)
        quick_sort_impl(lst, pivot + 1, upper_index)


# finding a pivot is a bit complex method, but the method places pivot in its correct position
def find_pivot(lst, lower, upper):
    i = lower - 1
    j = lower
    pivot = lst[upper]
    for j in range(lower, upper):
        if lst[j] < pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]  # elemets swapped
    lst[i + 1], lst[upper] = lst[upper], lst[i + 1]
    return i + 1


"""recursive algorithm - keep diving list into two until there are only two or one element and
 then merge them to the top"""


def merge_sort(lt):
    # divide list into two until there is only two or one element
    if len(lt) == 1:
        return lt
    elif len(lt) == 2:
        if lt[0] > lt[1]:
            lt[0], lt[1] = lt[1], lt[0]
        return lt
    else:
        middle_index = (len(lt) - 1) // 2
        # print(">>>>"+str(lt[0:middle_index]))
        lst1 = merge_sort(lt[0:middle_index])
        # print(">>>>" + str(lt[middle_index:]))
        lst2 = merge_sort(lt[middle_index:])
        return merge_list(lst1, lst2)


def merge_list(lst1, lst2):
    size1 = len(lst1)
    size2 = len(lst2)
    i = 0
    j = 0
    final_list = []

    while i < size1 and j < size2:
        if lst1[i] < lst2[j]:
            final_list.append(lst1[i])
            i = i + 1
        else:
            final_list.append(lst2[j])
            j = j + 1

    return final_list + lst1[i:] + lst2[j:]

"""insertion sort will iterate along the list and bring each element at correct position 
in ascending/desc order """

def insertion_sort(list1):

    for i in range(1, len(list1)):
        new_list = insert_algo(list1[i],list1[:i])
        list1 = new_list + list1[i+1:]

    return list1
# inserting an element at correct location in a list

def insert_algo(element,list11):
    pos = None
    for i in range(len(list11)):
        if element < list11[i]:
            pos = i
            break
        else:
            pass
    if pos is None:
        return list11+[element]
    else:
        return list11[:i]+ [element] + list11[i:]




if __name__ == "__main__":
    lst = [3, 8, 2, 1, 4]
    l = lst[:4] + [15] + lst[4:]
    #print(l)
    lst1 = [3, 8, 2, 1, 4, 5]
    # reference to the list is passed the elements are updated in the list
    # quick_sort(lst)
    #new_lst = merge_sort(lst)

    # print(merge_sort(lst))
    # print(merge_sort(lst1))
    # print(selection_sort(lst1))
    print(insertion_sort(lst1))
