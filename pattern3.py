class Solution:
    def pattern3(self, n):
        for i in range(n):
            for j in range(1, i+2):
                print(j, end="")
            print()


# Driving code
n = int(input("Enter N: "))

obj = Solution()
obj.pattern3(n)