def mergesort(arr,left,middle,right):
    i = left
    j = middle + 1
    temp = []
    while i <= middle or j <= right:
        while i <= middle and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        if i <= middle:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    for i in range(left,right+1):
        arr[i] = temp[i-left]

def count(arr,left,middle,right):
    cnt = 0
    i = middle + 1
    while left <= middle:
        while i <= right and arr[left] > 2*arr[i]:
            i += 1
        cnt += (i-(middle+1))
        left += 1
    return cnt

def merge(arr,left,right):
    cnt = 0
    if left >= right:
        return cnt
    middle = (left + right) // 2
    cnt += merge(arr,left,middle)
    cnt += merge(arr,middle+1,right)
    cnt += count(arr,left,middle,right)
    mergesort(arr,left,middle,right)
    return cnt 


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return merge(nums,0,len(nums)-1)
        