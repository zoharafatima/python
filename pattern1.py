class Solution:
    def pattern1(self, n):
        for i in range(n):
            print("*" * n)


# Driving code
n = int(input("Enter N: "))

obj = Solution()
obj.pattern1(n)