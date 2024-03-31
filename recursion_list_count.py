#an implementation of recursive function to count the number of items in a list 

def recursive_count(arr: list) -> int:
    #a function that is called recursively 
    
    if arr == []:
        #this is the base case i.e., when no items in the list remains to be counted
        return 0
    else:
        #this represents the recursive case i.e., length of array > 1, there are still
        # some items to be counted
        arr.pop()
        return 1+recursive_count(arr)
    
def main():
    my_list = ["ram", "hari", "sita"]
    print(f"number of items in the list = {recursive_count(my_list)}")

main()