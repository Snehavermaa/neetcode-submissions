class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Find pivot (smallest element)
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        # Binary search in the appropriate half
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1