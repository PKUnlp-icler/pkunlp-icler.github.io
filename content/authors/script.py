import os
import shutil

alumni_list = [
    "Ziqiang Cao",
    "Yi Cheng",
    "Wenyu Guan",
    "Decong Li",
    "Tianyi Li",
    "Xiangyang Li",
    "Qianying Liu",
    "Yang Liu",
    "Simin Rao",
    "Liang Wang",
    "Xun Wang",
    "An Yang",
    "Jingfeng Yang",
    "Qiusi Zhan",
    "Zhejian Zhou",
]

src_path = "./liyang/_index.md"
src_name = "Yang Li"

for idx, name in enumerate(alumni_list):
    dir_name = name.split(" ")
    dir_name = dir_name[-1:] + dir_name[:-1]
    dir_name = "".join(dir_name).lower()
    print(f"Processing No.{idx+1}: dir_name")
    dest_dir = f"./{dir_name}/"
    num = 10 * (idx+1)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    shutil.copy2(src_path, dest_dir)

    os.system(f"sed -i 's/{src_name}/{name}/g' {dest_dir+'_index.md'}")

    os.system(f"sed -i 's/10/{num}/g' {dest_dir+'_index.md'}")
