import os
print("""Choose from the options below ........
        1. Create new LV from VG 
        2. Display LVs
        3. Exit""")
while True : 
    c = input("Enter your choice : ")
    if int(c) == 1 :  
        vg = input("Enter the name of the Volume Group: ")
        lv = input("Enter the name to be allocated to the Logical Volume:")
        s = input("Enter the size of LV to be create : ")
        loc = input("Enter the path to attach the LVM :")
        os.system("lvcreate --size " + s + " --name " + lv + " " + vg)
        os.system("mkfs.ext4 /dev/" + vg + "/" + lv)
        os.system("mount /dev/" + vg + "/" + lv + " " + loc)

    elif int(c) == 2 :
        os.system("lvdisplay")
    elif int(c) == 3 :
        exit()
    else : 
        print("Choice not supported")


