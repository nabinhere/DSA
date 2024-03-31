def qsort(arr: list[int]) -> list[int]:
    # a function that implements the quicksort algorithm
    if len(arr) == 0 or len(arr) == 1:
        # no need to sort an array of length 0 or 1 -> base case
        return arr 
    elif len(arr) == 2:
        # an array of length 2 can be sorted easily -> also a base case
        return arr if arr[0]<arr[1] else [arr[1], arr[0]]
    else:
        #recursive_case
        pivot = arr.pop(0)      #treat first element as pivot
        left_list = [ x for x in arr if x <= pivot]     #list of elements <= pivot
        right_list = [ x for x in arr if x > pivot]     #list of elements > pivot
        return qsort(left_list) + [pivot] +qsort(right_list)    
        #recirsive function call to return a completely sorted list
    
def main():
    my_list = [3, 5, 2, 10, 12, 4, 17, 19, 5, 12]
    sorted_list = qsort(my_list)
    print(f"original list = {my_list}")
    print(f"sorted list = {sorted_list}")

main()
