class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count={}

        for num in nums:
            count[num] = count.get(num,0)+1;
        
        longest = 0
        for num in count:
            if num+1 in count:
                length= count[num] + count[num+1]
                longest = max(longest,length)
        return longest
        