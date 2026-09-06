class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = sorted(nums, reverse = True)
        self.k = k
        print(self.array)

    def add(self, val: int) -> int:
        self.array.append(val)
        self.array = sorted(self.array, reverse = True)
        return self.array[self.k - 1]

