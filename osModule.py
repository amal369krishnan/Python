import os
from datetime import datetime

# print(dir(os))

"""Changing current working directory path"""
# os.chdir('/home/rajeevam/Desktop')

"""getting cureent working directory"""
# print(os.getcwd())


"""creating new folder"""
# os.mkdir('python')
'''makedirs is more effecient to make subfolders instead of mkdir'''
# os.makedirs('python1/newfolder')

"""removing directries"""
# os.rmdir('python')
# os.removedirs('python1/newfolder')

"""Renaming the directories"""
# os.rename('text.txt','renamed_text')
# os.rename('python','Python')
 
# print(datetime.fromtimestamp(os.stat('renamed_text').st_atime))
'''listing directories'''
# print(os.listdir())

for dirname,dirpath,filenames in os.walk('/home/rajeevam/Desktop'):
	print('dirname',dirname)
	print('dirpath',dirpath)
	print('filenames',filenames)
	print()