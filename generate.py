#!/usr/bin/python3
import os

def create():
    with open('Dockerfile-template', 'r') as f:
        dockerfile = f.read()
        # check if package.txt exists
        if os.path.isfile('package.txt'):
            with open('package.txt', 'r') as f:
                package = f.read()
                # get value seperated by line break then transform it into string that seperated by space
                package = ' '.join(package.splitlines())
                dockerfile = dockerfile.replace('# packages.txt customization >>>', package)
                with open('Dockerfile', 'w') as f:
                    f.write(dockerfile)
        else:
            print('INFO: package.txt not found, straight copying Dockerfile-template to Dockerfile')
            with open('Dockerfile', 'w') as f:
                f.write(dockerfile)

if os.path.exists("Dockerfile"):
    print("Dockerfile exists, rebuilding it")
    os.remove("Dockerfile")
    create()
else:
    print("Dockerfile does not exist, creating it")
    create()