#!/usr/bin/python3
import subprocess

print("content-type: text/html")
print("""
<style>
    .table td {
        font-weight: normal;
    }
</style>
""")
print()

cmd="docker images"

exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

if exitCode == 0:
    totalContainer = output.split("\n")[1:]
    print("<table class='table table-hover table-bordered'>")
    print("""<thead>
        <tr>
        <th scope="col">REPOSITORY</th>
        <th scope="col">TAG</th>
        <th scope="col">IMAGE ID</th>
        <th scope="col">CREATED</th>
        <th scope="col">SIZE</th>
        </tr>
        </thead>""")

    for container in totalContainer:
        print("<tbody>")
        print("<tr>")
        print("<td>" + container.split()[0] + "</td>")  # REPOSITORY
        print("<td>" + container.split()[1] + "</td>")  # TAG
        print("<td>" + container.split()[2] + "</td>")  # IMAGE ID
        print("<td>" + " ".join(container.split()[3:7]) + "</td>")  # CREATED
        print("<td>" + container.split()[-1] + "</td>")  # SIZE
        print("</tr>")
        print("</tbody>")
    print("</table>")
else:
    print("command failed")

