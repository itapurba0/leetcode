class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = deque()

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or pairs[ch] != stack[-1]:
                    return False
                stack.pop()

        return not stack
