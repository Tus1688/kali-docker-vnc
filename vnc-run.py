#!/usr/bin/python3
import os

# check if Dockerfile is not exists
if not os.path.exists("Dockerfile"):
    print("You don't even create Dockerfile yet, create it first using generate.py, after that build it using build.py")
    exit()

try:
    os.system("docker run --name temp-kali --rm -p 5908:5908 -p 2022:2022 -v kali_data:/home/kali --cap-add=NET_ADMIN --device=/dev/net/tun -d kali/kali /startup.sh")
    print("VNC is running on port 5908\nSSH is running on port 2022\nuser: kali\npassword: kali\nyou can kill your container with kill-container.py")
except Exception as e:
    print(e)
    print("Something went wrong, please check your Dockerfile, is it correct?")
    exit()