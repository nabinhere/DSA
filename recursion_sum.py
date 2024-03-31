#an implementation of recursive function to find the sum of numbers in a list of integers

def recursive_sum(arr: list[int]) -> int:
    #a function that is called recursively 
    if len(arr) == 1:
        #this is the base case i.e., length of array = 1
        return arr[0]
    else:
        #this represents the recursive case i.e., length of array > 1
        return arr.pop(0)+recursive_sum(arr)
    
def main():
    my_list = [2,4,6,8,10]
    print(f"sum of the list = {recursive_sum(my_list)}")

main()