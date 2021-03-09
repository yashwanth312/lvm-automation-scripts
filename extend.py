import os

vg = input("Enter the name of Volume Group : ")
lv = input("Enter the name of Logical Volume : ")
size = input("Enter the size to extend to : ")

os.system("sudo lvextend --size " + size + " " + vg + "/" + lv)
os.system("sudo resize2fs /dev/" + vg + "/" + lv)

