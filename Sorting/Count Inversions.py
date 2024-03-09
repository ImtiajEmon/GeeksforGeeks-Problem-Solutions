class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        def mergeAndCount(arr1, arr2):
            # Count the inversions
            nonlocal ans
            i, j = 0, 0
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    ans += len(arr1) - i
                    j += 1
                else:
                    i += 1
                    
            # Now merge the arrays and return
            i, j = 0, 0
            merged_arr = []
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1
                    
            merged_arr += arr1[i:]
            merged_arr += arr2[j:]
            
            return merged_arr
            
            
        
        def count_inverse(arr):
            if len(arr) == 1:
                return arr
                
            mid = len(arr) // 2
            
            left_arr = count_inverse(arr[:mid])
            right_arr = count_inverse(arr[mid:])
            
            return mergeAndCount(left_arr, right_arr)
        
        ans = 0   
        count_inverse(arr)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
