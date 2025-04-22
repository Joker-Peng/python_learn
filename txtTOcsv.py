import csv

# 假设原始文件名为 'data.txt'
input_file = 'data.txt'
output_file = 'data.csv'

# 打开原始文件并读取内容
with open(input_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# 打开 CSV 文件并写入内容
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    # print(outfile)
    writer = csv.writer(outfile)
    #
    print(lines)
    for line in lines:
        # 去除每个元素中的\n
        if line!="\n":
            print(line)
            line.replace(",\n", "")
            print(line)
        else:
            continue
        exit()
        # print(line)
        # writer.writerow(line)
    #     # print(line)
    #     # if line=="[":
    #     #     print(line)
    #     if line=="\n":
    #         data = line+" "
    #     else:
    #         data = line
    # #     # 假设每行数据用空格分隔
    # #     data = line.strip().split()


# print(f"数据已成功转换为 CSV 格式并保存到 {output_file}")