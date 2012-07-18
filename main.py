#!/usr/bin/python
"""This is a simple script to organize files within your download folder
Author:Nithin Saji
Name:Py-Orgy
License:CC
"""
import re;
import shutil;
import os;
def copier(dir="."):
    print "time for orgy....."
    dirlist=os.listdir(dir)
    for d in dirlist:
        if(re.search(r'\.mp3$',d)):
            if not (os.path.isdir("music")):
                    os.mkdir("music");
            if(shutil.copy2(d,os.path.curdir+"/"+"music/"+d)):
                print d+" copied to music";


    print "organised";
        


def main():
    copier();
if __name__=="__main__":
    main();
