class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            t = target - nums[i]
            if t in nums and nums.index(t) != i:
                print('found')
                print(i, nums.index(t))
                return [i, nums.index(t)]
                break
            else:
                continue
        return None