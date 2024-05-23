import os

# 假设CSV文件在桌面上，并且桌面路径可以通过os.path.join(os.path.sep, 'Users', '你的用户名', 'Desktop')来获取
# 注意：这里的'你的用户名'需要替换为你的实际用户名
desktop_path = os.path.join(os.path.sep, 'Users', 'Administrator', 'Desktop')
input_csv_path = os.path.join(desktop_path, 'attack.csv')
output_csv_path = os.path.join(desktop_path, '阶段性考核.csv')

# 读取CSV文件
with open(input_csv_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 跳过标题行
header = lines[0]
data = lines[1:]

# 筛选重复数据（基于整行）
unique_data = []
seen_lines = set()
for line in data:
    if line not in seen_lines:
        unique_data.append(line)
        seen_lines.add(line)

    # 假设第一列是我们要排序的列（CSV文件以逗号分隔）
# 这里使用简单的字符串排序，对于数字可能需要额外的转换
unique_data.sort(key=lambda x: x.float(split(',')[0]), reverse=True)

# 写入新的CSV文件
with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
    file.write(header)  # 写入标题行
    for line in unique_data:
        file.write(line)  # 写入数据行

print(f"处理完成，结果已保存到 {output_csv_path}")