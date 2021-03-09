import os
print("""Choose from the options below ......
        1. Create a new VG 
        2. View VGs
        3. Exit""")
while True: 
    c = input("Enter your choice: ")
    if int(c) == 1 :
        pv = input("Enter names of the drivers: ")
        vg = input("Enter the name to be allocated to the created Volume Group: ")
        os.system("pvcreate " + pv)
        os.system("vgcreate --name " + vg + " " + pv)
        os.system("vgdisplay")
    elif int(c) == 2: 
        os.system("vgdisplay")
    elif int(c) == 3 :
        exit()
    else: 
        print("Choice not supported")

