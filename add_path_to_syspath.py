# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:09:00 2018

@author: zhouzian

"""

"""
将一个项目文件夹下所有有文件的目录导入到同一个list中，加入到pythonpath中
"""

import os
import sys

def add_path_to_syspath(rootdir):
    dir_list = list_all_files(rootdir)
    dir_list = {}.fromkeys(dir_list).keys()
    sys.path.extend(dir_list)
    
def list_all_files(rootdir):
    """
    'rootdir' - the root direction
    
    example:
    dir_list = list_all_files(r'C:\Users\a\Desktop\MyDeeplearning\Faster R-CNN\Faster-RCNN_TF-master')
    dir_list = {}.fromkeys(dir_list).keys()
    """
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    dir_path = rootdir
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):#是否是文件夹
            _files.extend(list_all_files(path)) 
        if os.path.isfile(path):
            _files.append(dir_path)
    return _files

    

if __name__ == '__main__':
    dir_list = add_path_to_syspath(r'C:\Users\a\Desktop\MyDeeplearning\Faster R-CNN\Faster-RCNN_TF-master')
    dir_list = {}.fromkeys(dir_list).keys()
    sys.path.extend(dir_list)
