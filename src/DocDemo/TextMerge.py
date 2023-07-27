import os

# 合并文件夹中的所有文件
def merge_files_in_folder(folder_path, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath) and filename.endswith('.sql'):
                with open(filepath, 'r') as input_file:
                    output.write(input_file.read())
                    # 如果希望在合并的文件之间加入分隔符，可以使用下面这行代码
                    # output.write('\n')

# 要合并的文件夹路径
folder_path = 'C:/Users/lenovo/Desktop/sql'

# 合并后的输出文件
output_file = 'merged_file.sql'

# 调用函数进行合并
merge_files_in_folder(folder_path, output_file)
