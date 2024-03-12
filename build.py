#!/usr/bin/python


import os
import threading
import sys

runing = True


def readfile(logfile):
    with open(logfile, 'w') as f:
        pass
    with open(logfile, 'r') as f:
        while runing:
            line = f.readline(1000)
            if line != '':
                line = line.replace('\\', '/')
                print(line, end='')


if __name__ == '__main__':
    modulePath = os.path.abspath(os.curdir)
    logfile = modulePath + '/.vscode/build.log'
    cmd = ''
    for i in range(1, len(sys.argv)):
        cmd += sys.argv[i] + ' '
    cmd += '-j0 -o ' + logfile
    print(cmd)
    thread = threading.Thread(target=readfile, args=(logfile,))
    thread.start()
    code = os.system(cmd)
    runing = False
    thread.join()
    sys.exit(code)
