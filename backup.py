#源文件夹和备份文件夹比较，创建和修改新文件但不能删除备份文件夹不需要的文件/夹
import os, sys
import filecmp
import re
import shutil

holderlist = []

#递归获取更新
def compareme(dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2)
    #源目录中的新文件或目录
    only_in_src = dircomp.left_only
    #更新的文件或目录
    diff_in_src = dircomp.diff_files
    dirpath = os.path.abspath(dir1)
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_src]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_src]
    #判断有没相同子目录以执行递归
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
        return holderlist

def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print("Usage: {} datedir backupdir".format(sys.argv[0]))
        sys.exit()
    source_files = compareme(dir1, dir2)
    dir1 = os.path.abspath(dir1)

    if not dir2.endswith('/'): dir2 += '/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    for item in source_files:
        #将源目录差异路径替换成备份目录路径
        destination_dir = re.sub(dir1, dir2, item)
        destination_files.append(destination_dir):
            os.makedirs(destination_dir)
            createdir_bool = True

    #再次调用compareme，重新遍历新创建目录中的内容
    if createdir_bool:
        destination_files = []
        source_files = []
        source_files = compareme(dir1, dir2)
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print("update item:")
    print("{}".format(source_files))
    #将存在差异的源文件和备份文件拆分成元祖对
    copy_pair = zip(source_files, destination_files)
    for item in copy_pair:
        #判断是否是文件，是则进行复制
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])

if __name__ == '__main__':
    main()
