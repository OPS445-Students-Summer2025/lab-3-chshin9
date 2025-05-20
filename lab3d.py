#!/usr/bin/env python3
'''Lab 3 return free space of Linux system root dir'''
# Author ID: cshin9

import subprocess

def free_space():
    space = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = space.communicate()[0]
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
