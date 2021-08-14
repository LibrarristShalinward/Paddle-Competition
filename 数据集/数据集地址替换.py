# 犯大病：我偏不用非中文变量名
原始标注路径 = "testdev2017.txt"
输出路径 = "标注.txt"
数据集说明路径 = "关于COCO数据集.txt"

with open(数据集说明路径, "r", encoding = "UTF-8") as 数据集说明文件:
    数据集路径 = [行 for 行 in 数据集说明文件.readlines()][3][:-1]

with open(原始标注路径, "r") as 原始标注文件:
    with open(输出路径, "w") as 输出文件:
        for 行 in 原始标注文件.readlines():
            新路径 = 数据集路径 + 行[-16:]
            输出文件.write(新路径)