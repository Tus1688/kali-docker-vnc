#!/usr/bin/python3
import os

# check if Dockerfile is not exists
if not os.path.exists("Dockerfile"):
    print("You don't even create Dockerfile yet, create it first using generate.py, after that build it using build.py")
    exit()

try:
    print("running interactive mode")
    os.system("docker run --name temp-kali --rm -v kali_data:/home/kali -u kali -w /home/kali --cap-add=NET_ADMIN --device=/dev/net/tun -it kali/kali")
except Exception as e:
    print(e)
    print("Something went wrong, please check your Dockerfile, is it correct?")
    exit()