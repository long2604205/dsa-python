from algorithms.sorting.quick_sort import quick_sort
from utils.helpers import print_list

if __name__ == "__main__":
    arr = [5,1,4,2,8]
    print_list("Original", arr)
    sorted_arr = quick_sort(arr)
    print_list("Sorted", sorted_arr)
