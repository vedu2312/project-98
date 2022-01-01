import os
import shutil


#source=input("enter source folder:")
#dast=input("enter source folder:")
source="C:/Users/vishal/Desktop/python/c99/newfloder/file1.txt"
dast="C:/Users/vishal/Desktop/python/c99/file2.txt"
shutil.copy(source,dast)
print("file copy")