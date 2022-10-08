# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         i = 0
#         nums2 = []
#         while i < len(nums):
#             if nums[i] in nums2:
#                 i += 1
#                 continue
#             else:
#                 nums2.append(nums[i])
#                 i += 1
#                 continue
#         return len(nums2)

def removeDuplicates(nums):
        i = 0
        nums2 = []
        for i in nums:
            if i in nums2:
                continue
            else:
                nums2.append(i)

        print(nums2)
        return len(nums2)

removeDuplicates([1,1,2])

        # while i < len(nums):
        #     if nums[i] in nums2:
        #         i += 1
        #         continue
        #     else:
        #         nums2.append(nums[i])
        #         i += 1
        #         continue
        # return len(nums2)