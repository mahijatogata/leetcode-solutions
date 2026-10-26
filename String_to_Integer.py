class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        while i < n and s[i] >= '0' and s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                if sign == -1:
                    return INT_MIN
                return INT_MAX

            num = num * 10 + digit
            i += 1

        return num * sign
