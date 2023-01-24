def insertion_sort(a):
    # A list of length 0 or 1 is already sorted
    if len(a) == 0 or len(a) == 1:
        return a

    # Remove the head of the list for the next recursive call
    recursive_list = insertion_sort(a[1:])

    # Sort the head of the list with the results of the recursive calls
    sorted_list = place_in_list(a[0], recursive_list, 0)
    return sorted_list


def place_in_list(head, tail, i):
    # Arrived at the end of the list without finding a value smaller than head, so it belongs at the end of the list
    if i >= len(tail):
        sorted_list = tail + [head]
        return sorted_list

    # The current tail element's value is less than the value of head, thus the head belongs after that element
    if head < tail[i]:
        sorted_list = tail[0:i] + [head] + tail[i:]
        return sorted_list

    # Recursive call to check next position in the tail list
    return place_in_list(head, tail, i + 1)


# Test cases
print(insertion_sort([0, 5, 1, 2, 4, 3]))
print(insertion_sort([120, 125, 1, 552, 24, 321]))
print(insertion_sort([100]))
print(insertion_sort([]))
