import pandas as pd

# 读取第一个文件，包含姓名和学号
file1 = pd.read_excel('【总表】南方科技大学2023级学生军事技能成绩表(1).xlsx') # fudaoyuan

# 读取第二个文件，只包含姓名
file2 = pd.read_excel('【总表】南方科技大学2023级学生军事技能成绩表(2).xlsx') # xuehao

print(file1.describe())
print(file2.describe())

# 使用merge函数将两个文件根据姓名进行左连接，并将学号列重命名为"学号"
merged_file = pd.merge(file2, file1, on='姓名', how='left')

print(merged_file.describe())

merged_file.drop([i for i in file2.columns])

# 保存结果到新的Excel文件
merged_file.to_excel('merged_file.xlsx', index=False)

