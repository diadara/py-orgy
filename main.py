#!/usr/bin/python
"""This is a simple script to organize files within your download folder
Author:Nithin Saji
Name:Py-Orgy
License:CC
"""
def copier(dir="."):
    import os;
    print "time for orgy....."
    dirlist=os.listdir(dir)
    for d in dirlist:
           print os.path.curdir+d
        


def main():
    copier();
if __name__=="__main__":
    main();
