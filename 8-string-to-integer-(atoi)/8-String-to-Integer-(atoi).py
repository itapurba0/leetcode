class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] in ['-','+']:
            sign = -1 if s[0] == '-' else 1
            s= s[1:]

        i = 0
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        num *= sign
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num
