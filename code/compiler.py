# BUG: Next line not working like string keywords like \n, \t, \b
# BUG: Remove file name



#!/usr/bin/env python3
import subprocess
import sys

# read the input file
r = open('/var/www/html/GamifyString/code/input.txt', "r")
inp = r.readline()
r.close

fileType = sys.argv[1]

#compile the
#def compil(args)

#run the code on linux enviornment
def executecpp():
    subprocess.call(["/usr/bin/g++", "/var/www/html/GamifyString/code/gamify.cpp"])
    proc = subprocess.Popen("/var/www/html/GamifyString/phpfunctions/a.out", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(str.encode(inp), timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate(inp)

    if outs:
        out = bytes.decode(outs)
    else:
        out = bytes.decode(errs)
    return out
    # tmp=subprocess.call("/var/www/html/GamifyString/phpfunctions/a.out")
    # tmp = tmp[:-1]
    # return tmp

def executejava():
    subprocess.call(["/usr/bin/javac", "/var/www/html/GamifyString/code/gamify.java"])
    proc = subprocess.Popen(["/usr/bin/java", "gamify"], cwd="/var/www/html/GamifyString/code/", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(str.encode(inp), timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate(inp)

    if outs:
        out = bytes.decode(outs)
    else:
        out = bytes.decode(errs)
    return out
    # tmp=subprocess.call(["/usr/bin/java", "gamify"], cwd="/var/www/html/GamifyString/code/")
    # tmp = tmp[:-1]
    # return tmp

def executepython():
    proc = subprocess.Popen(["/usr/bin/python3", "/var/www/html/GamifyString/code/gamify.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(str.encode(inp), timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate(inp)

    if outs:
        out = bytes.decode(outs)
    else:
        out = bytes.decode(errs)
    return out

#check the file type
if fileType == "python":
    print(executepython())
if fileType == "c_cpp":
    print(executecpp())
if fileType == 'java':
    print(executejava())
