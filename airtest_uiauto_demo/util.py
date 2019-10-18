# -*- coding: utf-8 -*-

import inspect
import os, zipfile
from os.path import join
from datetime import date
from time import time
from zipstest import *
def img(name):
    folder = inspect.stack()[1][1]
    index = folder.find(".")
    if index >= 0:
        folder = folder[ : folder.find(".")]
    folder = os.path.join(folder, name) + ".png"
    return folder

#打包目录为zip文件（未压缩）



def zip_folder(foldername, filename):
    zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(foldername):
        # files of cur file
        for filename in files:
            print("compressing", join(root, filename).encode("gbk"))
            zip.write(join(root, filename).encode("gbk"))

        # empty dir
        if len(files) == 0:
            print('empty dir')
            zif = zipfile.ZipInfo((root + '/').encode("gbk" + "/"))
            zip.writestr(zif, "")
    zip.close()
    print("Finish compressing")

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
    print(r"%s"%(os.path.dirname(os.path.abspath(__file__))))
    print(os.path.dirname(__file__))
    #zip_file_path(r".\air_case", 'D:', 'multireport.zip')