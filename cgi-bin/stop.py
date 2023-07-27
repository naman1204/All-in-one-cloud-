#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import dockerlistmodule
import cgi

form = cgi.FieldStorage()
container_name = form.getvalue('container_name')

command="docker stop "+container_name
output1=subprocess.getoutput("sudo "+command)
