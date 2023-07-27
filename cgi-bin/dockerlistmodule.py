#!/usr/bin/python3

import subprocess

def dockerTable():
    cmd = "docker ps"
    exitCode , output = subprocess.getstatusoutput("sudo " + cmd)

    if exitCode == 0:
        totalContainer = output.split("\n")[1:]

        print("<table class='table table-hover table-bordered'>")
        print("""<thead>
                <tr>
                <th scope="col">Console</th>
                <th scope="col">Status</th>
                <th scope="col">Image</th>
                <th scope="col">Name</th>
                <th scope="col">Start</th>
                <th scope="col">Stop</th>
                </tr>
                </thead>""")

        for container in totalContainer:
            print("<tbody>")
            print("<tr>")
            print("<td>" +  "<a onclick='scrollToBottom()' target='myos' href='https://13.232.124.244:4200'>Console</a>" + "</td>")
            print("<td>" + container.split()[6] + "</td>")
            print("<td>" + container.split()[1] + "</td>")
            container_name = container.split()[-1]
            print("<td>" + container_name + "</td>")
            print("<td>" +  "<button class='btn btn-outline-secondary' onclick='startContainer(containerName)' type='button'>Start</button>" + "</td>")
            print("<td>" +  "<button class='btn btn-outline-secondary'onclick=''' type='button'>Stop</button>" + "</td>")
            print("</tr>")

        print("</table>")
        print("""
        <script>
        function startContainer(containerName) {
            var xhttp = new XMLHttpRequest();
            xhttp.open("POST", "http://13.232.124.244/cgi-bin/stop.py", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send("container_name=" + container_name);
        }

        function stopContainer(containerName) {
            var xhttp = new XMLHttpRequest();
            xhttp.open("POST", "http://13.232.124.244/cgi-bin/start.py", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send("container_name=" + container_name);
        }
        </script>
        """)

    else:
        print("command failed")

