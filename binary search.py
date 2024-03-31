def binary_search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low+high)/2)
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid +1
        else:
            high = mid -1
    return None

def main():
    test_list = [1,3,5,7,9]
    target1 = 7
    target2 = -1
    print(f"The number {target1} is in the index {binary_search(test_list, target1)} of test_list")
    print(f"The index of {target2} in test_list = {binary_search(test_list, target2)}")

main()
    
    