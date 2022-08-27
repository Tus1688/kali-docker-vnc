#!/usr/bin/python3
import os

# check if Dockerfile exists
if os.path.exists("Dockerfile"):
    os.system("docker build -t kali/kali:latest .")
else:
    print("You don't even create Dockerfile yet, create it first using generate.py")