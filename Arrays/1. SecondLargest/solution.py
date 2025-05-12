class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = sec_largest = -1
        
        for i in arr:
            if i > largest:
                sec_largest = largest
                largest = i
            elif largest > i > sec_largest:
                sec_largest = i
        
        return sec_largest

#{ 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends