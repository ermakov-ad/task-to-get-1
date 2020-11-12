import pathlib
import shutil
import os
import requests

path = str('C:\\Users\\Admin\\Documents\\py') + "\\icons"
print(path)

try:
    shutil.rmtree(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

# https://icons8.com/icons/set/name

names = {'python', 'c-plus-plus-logo'}

iconSize = {"50": '50', "100": '100'}
iconTheme = 'ios'
colors = {'blue ': '005EB8', 'orange ': 'FF9919'}

for key in iconSize:

    colorPath = path + '\\' + key

    try:
        os.mkdir(colorPath)
    except OSError:
        print ("Creation of the directory %s failed" % colorPath)   #ЕРМАКОВ АЛЕКСЕЙ
    else:
        print ("Successfully created the directory %s " % colorPath)

    for n in names:
        for i in colors:
            name = n + ".png"
            r = requests.get('https://img.icons8.com/' + iconTheme + '/' + colors[i] + '/' + iconSize[key] + '/' + name , allow_redirects=True)
            open(colorPath + '/' + i + name, 'wb').write(r.content)