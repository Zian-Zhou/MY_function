# MY_function
I have write some function to solve the proplems that I met during my study

####1.add_path_to_syspath.py
将一个项目文件夹下所有有文件的目录导入到同一个list中，加入到pythonpath中
       dir_list = add_path_to_syspath(yourfile)
       dir_list = {}.fromkeys(dir_list).keys()
       sys.path.extend(dir_list)