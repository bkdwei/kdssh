# coding: utf-8
import os
def check_and_create(absolute_file_path):
    slash_last_index = absolute_file_path.rindex("/")
    path = absolute_file_path[:slash_last_index]
    file = absolute_file_path[slash_last_index + 1:]
    print(path)
    print(file)
    # 检查目录
    if os.path.exists(path) is not True:
        os.makedirs(path)
    elif os.path.isdir(path) is not True :
        print(path,"is no a dir,delete and create a dir")
        os.remove(path)
        os.makedirs(path)
    # 检查文件
    if os.path.exists(absolute_file_path) is not True:
        with open(absolute_file_path,'w+') as f:
            pass
    elif os.path .isfile(absolute_file_path) is not True :
        os.removedirs(absolute_file_path)
        with open(absolute_file_path,'w+') as f:
            pass
if __name__ == '__main__':
    a = "./u/y/p.jpg"
    print(dir(os.path))
    print(dir(os))
    check_and_create(a)