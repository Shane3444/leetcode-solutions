# def rotateOnce(arr):
#     i = 0
#     j = -1
#     while i < len(arr):
#         t = arr[i]
#         arr[i] = arr[j]
#         arr[j] = t
#         i += 1

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
        # k = k % len(nums)
        # if k < 0 : 
        #     k += len(nums)
        # for i in range(0,k):
        #     rotateOnce(nums)
            