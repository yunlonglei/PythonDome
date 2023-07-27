import os
import sys

def merge_sql_files_in_folder(folder_path, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath) and filename.endswith('.sql'):
                with open(filepath, 'r') as input_file:
                    output.write(input_file.read())
                    # 如果希望在合并的文件之间加入分隔符，可以使用下面这行代码
                    # output.write('\n')

# python merge_sql_files.py /path/to/your/folder /custom/output/path/ merged_sql_file.sql
# 其中，/path/to/your/folder是要合并的文件夹路径，/custom/output/path/是自定义的输出文件夹路径，merged_sql_file.sql是输出文件的名称。
# 脚本将会把该文件夹下的所有以'.sql'结尾的SQL文件合并成一个文件，并保存到/custom/output/path/目录下的merged_sql_file.sql文件中。
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_sql_files.py folder_path output_file_path output_file_name")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file_path = sys.argv[2]
    output_file_name = sys.argv[3]
    output_file = os.path.join(output_file_path, output_file_name)

    merge_sql_files_in_folder(folder_path, output_file)
