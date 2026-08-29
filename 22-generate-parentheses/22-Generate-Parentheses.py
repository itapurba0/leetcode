class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(curr_string,openCount,closeCount):
            if len(curr_string) == 2*n:
                result.append(curr_string)
                return
            if openCount < n:
                backtrack(curr_string+"(",openCount+1,closeCount)
            if closeCount < openCount:
                backtrack(curr_string+")",openCount,closeCount+1)

        backtrack("",0,0)
        return result

        