#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import dockerlistmodule
import cgi

form = cgi.FieldStorage()
container_name = form.getvalue('containerName')

def stop_container():
    command="docker stop "+containerName
    output1=subprocess.getoutput("sudo "+command)

def start_container():
    command1="docker start " +containerName
    output2=subprocess.getoutput("sudo "+command1)




