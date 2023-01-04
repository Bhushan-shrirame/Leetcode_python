class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # length of array
        n = len(arr) -1
        # last element
        maxsf = arr[n]
        for i in range(n,0,-1):
            # latest maximum element
            temp  = arr[i-1]
            # assigning value to array
            arr[i-1] = maxsf
            # checking for max element
            if temp > maxsf :
                maxsf = temp
        arr[-1] = -1
        return arr            
