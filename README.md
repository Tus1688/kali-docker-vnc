# kali-docker-vnc
easily build & run kali linux on docker while utilizing the power of vnc

![kali-docker-vnc](./kali-docker-vnc.png)

# Features:
The only persistent is `/home/kali`. Let's say you got pwned by malicious script, 
that successfully escalates to root and manages to create super sneaky persistence in `/root`, modifying `/etc/hosts`,
installing something in `/usr/bin`. Luckily, **It won't be happen here**, as everything except `/home/kali`
will be **disposed** following shutdown.
However, it's **still possible to add malicious hooks in `/home/kali`** for example `.zshrc` or `.profile`, which will be run everytime you open zsh, and surely
many others places.

# Important notes:
`kali_data` is docker volume that will be binded upon container creation, your customization will be kept there. If you think your `/home/kali` is compromised,
just delete `kali_data`.

# How to use:
1. `git clone https://github.com/Tus1688/kali-docker-vnc`
2. Create `package.txt`
3. Fill it with packages you want to install, for example:
```
tool1
tool2
tool3
````
4. Generate Dockerfile by running `python3 generate.py`
5. Build docker image by running `python3 build.py`
6. Run it, `python3 run.py` for cli only or `python3 vnc-run.py` to start with vnc and ssh
7. Profits 🤑
8. If you use vnc then you can kill your container with `python3 kill-container.py`

# Disclaimer 
Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user’s responsibility to obey all applicable local, state and federal laws. We assume no liability and are not responsible for any misuse or damage caused by this tool.
