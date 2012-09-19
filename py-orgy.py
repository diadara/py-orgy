#!/usr/bin/python2
"""This is a simple script to organize files within your download folder
Author:Nithin Saji
Name:Py-Orgy
License:CC
"""
import re;
import shutil;#for copying files
import sys;
import os;
def copier(dir="."):
    print "time for orgy....."
    dirlist=os.listdir(dir)
    for d in dirlist:
        if(re.search(r'(?:\.mp3$)|(?:\.wav$)|(?:\.flac$)',d,re.I)):
            print d+" found";
            if not (os.path.isdir("music")):
                    os.mkdir("music");
            shutil.move(d,dir+'/'+'music'+'/'+d);
        elif(re.search(r'(?:\.flv$)|(?:\.mp4$)|(?:\.avi$)|(?:\.mkv$)|(?:\.webm$)',d,re.I)):
            print d+ " found";
            if not (os.path.isdir("videos")):
                os.mkdir("videos");
            shutil.move(d,dir+'/'+'videos'+'/'+d);
        elif(re.search(r'(?:\.doc[x]?$)|(?:\.pdf$)|(?:\.txt$)',d,re.I)):
            if not os.path.isdir("docs"):
                os.mkdir("docs");
            shutil.move(d,dir+'/'+'docs'+'/'+d);
        elif(re.search(r'(?:\.exe$)|(?:\.zip$)|(?:\.tar\.?)',d,re.I)):
            if not os.path.isdir("exe_n_comp"):
                os.mkdir("exe_n_comp");
            shutil.move(d,dir+'/'+'exe_n_comp'+'/'+d);
    print "organised";


def main():
          copier();
if __name__=="__main__":
    main();
