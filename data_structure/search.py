class Search:

    """linear search - because time taken increases with number of elements.
    more the number of elements more is the time taken"""

    def linear_search(self,element):
        for elem in lst:
            if elem == element:
                return True
            else:
                return False

    """linear search - because time taken increases with number of elements.
        more the number of elements more is the time taken - complexity = O(log(n))
        
        1 = 1 
        2 = 1
        4 = 2
        8 = 3
        
        """

    def binary_search(self,lt,element,first_index=None,last_index=None):
        if first_index is None and last_index is None :
            middle_index = (len(lt)-1)//2
            first_index = 0
            last_index = len(lt)-1
        else:
            middle_index = (first_index+last_index)//2
        #print(">>>>"+str(first_index)+">>"+str(last_index)+">>"+str(middle_index))
        if middle_index == 0:
            print("Element Not Found")
            return None
        else:
            if lt[middle_index] == element:
                return middle_index
            elif lt[middle_index] > element:
                return self.binary_search(lt,element,first_index,middle_index-1)
            else:
                return self.binary_search(lt, element,middle_index+1,last_index)

if __name__== "__main__":
    lst = []
    lst1 = [0,1,2,3,4,5,6]
    srch = Search()
    print("index of element found is " + str(srch.binary_search(lst1,1)))