class SelectionSort():
    def __init__(self, arr:list[int] = []):
        self.arr = arr

    def sort(self, arr: list[int]) -> list[int]:
        sorted_array = []
        self.arr = arr
        for i in range(len(self.arr)):
            min = self.find_min(self.arr)
            sorted_array.append(min)
            arr.remove(min)
        return sorted_array

    def find_min(self, arr:list[int]) -> int:
        min = arr[0]
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
        return min


def main():
    my_list = [16,-45,29,-18,7,36,-3,-21,11,44]
    my_sort = SelectionSort()
    print(f"Here is the sorted list: {my_sort.sort(my_list)}")

main()

