
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    i = 0
    # while guessed length is less than actual
    for j in range(n):

        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
    # Add 1 for length
    return i + 1