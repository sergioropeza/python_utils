from pathlib import Path

root_path = '/opt/DEV/AITIC-Workspace/odoo15/custom-kitsolar/KITSOLAR_SH/'
addons = []
with open(root_path+".gitmodules") as fname:
    lines = fname.readlines()
    for line in lines:
        if 'path' in line:
            addon_path = root_path + line.split("=")[1].strip()
            addons.append(addon_path)

print("%s, %s" % ( root_path,str(addons).replace("[", "").replace("]", "").replace("'", "")))
