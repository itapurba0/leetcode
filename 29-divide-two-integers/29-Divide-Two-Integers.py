class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2147483647
        MIN_INT = -2147483648

        is_negative = (dividend < 0 ) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotent = 0
        while dividend >= divisor:
            curr_scoop = divisor
            scoops= 1

            while dividend >= (curr_scoop+curr_scoop):
                curr_scoop += curr_scoop
                scoops += scoops

            dividend -= curr_scoop
            quotent += scoops
        if is_negative:
            quotent = -quotent

        return min(max(MIN_INT,quotent),MAX_INT)