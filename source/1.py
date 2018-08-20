class Solution:
    def twoSum(self, nums, target):
        for index, v1 in enumerate(nums):
            v2 = target - v1
            new_list = nums[index + 1:]
            try:
                index2 = new_list.index(v2)
            except:
                continue
            if index2 != -1:
                return [index, index + 1 + index2]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1, 2, 3, 8], 5))
