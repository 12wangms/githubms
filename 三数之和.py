def threeSum(nums):
    nums.sort()  # 先对数组进行排序  
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的数字  
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 跳过重复的数字  
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # 跳过重复的数字  
                    right -= 1
                left += 1
                right -= 1
    return result


# 示例
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))