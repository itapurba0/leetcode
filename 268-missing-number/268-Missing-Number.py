class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # expected_sum = n * (n+1) // 2
        # total = sum(nums)
        # return expected_sum - total

        # Using XOR
        result = n
        for i in range(n):
            result ^= i ^ nums[i]
        return result
