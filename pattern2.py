class Solution:
    def pattern2(self, n):
        for i in range(n+1):
            print("*"*i)

N=int(input("Enter N: "))

obj=Solution()
obj.pattern2(N)