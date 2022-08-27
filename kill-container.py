#!/usr/bin/python3
import os

# kill container
try:
    # receive input from user
    inp = input("Are you sure you want to kill your container? (y/n) ")
    if inp == 'y':
        os.system("docker kill temp-kali")
except Exception as e:
    print(e)
    exit()