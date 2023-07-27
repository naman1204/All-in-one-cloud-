#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import dockerlistmodule
import cgi

form = cgi.FieldStorage()
container_name = form.getvalue('containerName')

command1="docker start " +container_name
output2=subprocess.getoutput("sudo "+command1)

