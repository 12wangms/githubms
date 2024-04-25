def twoSum(nums, target):
    # 创建一个空字典用于存储数组元素及其索引
    num_dict = {}

    # 遍历数组
    for i, num in enumerate(nums):
        # 计算目标值与当前值的差
        complement = target - num

        # 检查差是否在字典中
        if complement in num_dict:
            # 如果在，返回结果
            return [num_dict[complement], i]

            # 如果差不在字典中，将当前值和其索引加入字典
        num_dict[num] = i

        # 如果没有找到满足条件的两个数，返回空列表
    return []