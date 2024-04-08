"""
    The merge sort algorithm:
            -> In this .py file, we are coding the merge sort algorithm 
            -> We have an array and we want to sort the elements 
            -> We take this, and divide it into two 
            -> We repeat this division process until we have many smaller lists, each which contain 
                individual elements from the larger array
            -> These are then compared and sorted
            -> Once this recursion process is complete, the ordered sub-lists are put back together 
                into a sorted version of the original array 

    The `merge_sort` function:
        -> The function is called `merge_sort`, and the input to the function is the array which we 
            want to sort
        -> If the element which is inputted into the function is a single number, then its output is 
            the same as its input (there is nothing to sort)
"""

def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

"""
    Dividing the input array:
        -> If the array contains a larger amount of elements, we divide it into two - by finding the 
            central one <- This is the 'middle point' of our array, and each of the parts on either 
                side of it are the `left_part` and `right_part`
        -> We repeat this process recursively, to break the input array into two again and again 
        -> Eventually, the entire thing is broken down into multiple lists, with each list being an 
            element in the original input array 

    Sorting and merging the array:
        -> So we have taken the input array and broken it down into multiple smaller lists 
        -> Each of those lists representing an original element in the input array 
        -> Then we order them by selecting the smaller ones first, and merging them back into an output 
            array - as part of the sorting algorithm  (`merge_sort`)
        -> While we do this, we have two halves of a larger list and are comparing them 
        -> We are iterating through the sets of elements from the two halves, comparing them and selecting 
            the smaller one 
        -> Then populating the `array` variable with it 
        -> Carrying this on until we exhaust all of the list elements 
        -> Once the `array` variable has been sorted, the function then returns it 
"""

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

"""
    Testing the function:
        -> We are inputting an array into the function  
        -> And testing it to see if this outputs the sorted array (which in this case it does)
        -> This tests it on the `[4, 10, 6, 14, 2, 1, 8, 5]` example array 
        -> It is printing the unsorted array, and then the sorted one using the `merge_sort` function 
"""

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))
