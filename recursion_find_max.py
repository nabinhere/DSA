#an implementation of recursive function to find the maximum number in a list of integers

def recursive_max(arr: list[int]) -> int:
    #a function that is called recursively 
    
    if len(arr) == 1:
        #this is the base case i.e., when no items in the list remains to be counted
        return arr[0]
    else:
        #this represents the recursive case i.e., length of array > 1, there are still
        # some items to be counted
        arr.pop()
        return 1+recursive_max(arr)
    
def main():
    my_list = ["ram", "hari", "sita"]
    print(f"number of items in the list = {recursive_max(my_list)}")

main()