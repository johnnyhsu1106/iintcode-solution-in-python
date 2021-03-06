'''
Given an array of integers,
find how many unique pairs in the array
such that their sum is equal to a specific target number.
Please return the number of pairs.

Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) <= 1:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        num_of_pairs = 0

        while left < right:
            total = nums[left] + nums[right]

            if total > target:
                right -= 1

            elif total < target:
                left += 1

            else:
                num_of_pairs += 1
                left += 1
                right -= 1
                # skip the duplicate (inner loop: nleft <right must be satisfied)
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return num_of_pairs



# def main():
#     s = Solution()
#     nums = [7, 1, 1, 2, 3, 4]
#     target = 3
#     print(s.twoSum6(nums, target))
#
# if __name__ == '__main__':
#     main()
