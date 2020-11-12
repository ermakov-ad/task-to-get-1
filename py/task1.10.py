import pathlib
import shutil
import os
import requests

path = str('C:\\Users\\Admin\\Documents\\py') + "\\icons.ocean"
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

# https://oceancolor.gsfc.nasa.gov/l3/
# ЕРМАКОВ АЛЕКСЕЙ 
names = []

for i in range(3, 18, 1):

    names.append('%s sep 2020' % i)

iconSize = {"4km": '4km', "9km": '9km'}

for key in iconSize:

    colorPath = path + '\\' + key

    try:
        os.mkdir(colorPath)
    except OSError:
        print ("Creation of the directory %s failed" % colorPath)
    else:
        print ("Successfully created the directory %s " % colorPath)
    
    for i in names:
        for j in range(3, 18, 1):
            name = i + ".png"
            if j<10:
                r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST4/L3/2020/090' + str(j) + '/AQUA_MODIS.2020090' + str(j) + '.L3m.DAY.SST4.sst4.' + str(iconSize[key]) + '.NRT.nc.png' , allow_redirects=True)
                open(colorPath + '/' + name, 'wb').write(r.content)
            else:
                r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST4/L3/2020/09' + str(j) + '/AQUA_MODIS.202009' + str(j) + '.L3m.DAY.SST4.sst4.' + str(iconSize[key]) + '.NRT.nc.png' , allow_redirects=True)
                open(colorPath + '/' + name, 'wb').write(r.content)