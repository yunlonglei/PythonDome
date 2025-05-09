def filter_log_by_string(log_file_path, string_to_find, output_file_path=None):
    matched_lines = []
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if string_to_find in line:
                matched_lines.append(line)

    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(matched_lines)

    return matched_lines

# 示例
log_file = '/Users/leiyunlong/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/AE2D75698DBDDA7774A1C84404559C93/Caches/Files/2025-04/69bc0da3720f3106e4d991da50af53e9/2025-04/pmtl-batch-info-2025-04-07-1.log'
string = '1bf92af397e94ade'
output_file = 'filtered_log.log'

matched = filter_log_by_string(log_file, string, output_file)

# 打印结果
for line in matched:
    print(line.strip())
