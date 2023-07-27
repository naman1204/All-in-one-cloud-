#!/usr/bin/python3

import subprocess

def centosLatest():

    cmd="docker run -dit centos"

    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode==0:
        print("Image ID: "+output)
    else:
        print("cmd failed")


def rhelLatest():

    cmd="docker run -dit redhat/ubi8"

    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode==0:
        print("Image ID: "+output)
    else:
        print("cmd failed")

def ubuntuLatest():

    cmd="docker run -dit ubuntu"

    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode==0:
        print("Image ID: "+output)
    else:
        print("cmd failed")

def sinaboxLatest():

    cmd="docker run -p 4200:4200 -e SIAB_PASSWORD=redhat -e SIAB_SUDO=true sspreitzer/shellinabox:latest"

    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode==0:
        print("Image ID: "+output)
    else:
        print("cmd failed")



def fedoraLatest():

    cmd="docker run -dit fedora"

    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode==0:
        print("Image ID: "+output)
    else:
        print("cmd failed")

