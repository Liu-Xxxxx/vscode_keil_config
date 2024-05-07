#!/usr/bin/python

import os
import threading
import sys

running = True

def readfile(logfile):
    with open(logfile, 'w') as f:
        pass
    with open(logfile, 'r') as f:
        while running:
            line = f.readline(1000)
            if line != '':
                line = line.replace('\\', '/')
                print(line, end='')

if __name__ == '__main__':
    modulePath = os.path.abspath(os.curdir)
    logfile = modulePath + '/.vscode/build.log'
    cmd = ""
    for i in range(1, len(sys.argv)):
        # 如果是路径参数，确保用双引号括起来
        if os.path.exists(sys.argv[i]):
            cmd += '"' + sys.argv[i] + '" '
        else:
            cmd += sys.argv[i] + ' '
    cmd += '-j0 -o ' + '"' + logfile + '"'
    print(cmd)
    thread = threading.Thread(target=readfile, args=(logfile,))
    thread.start()
    # 使用subprocess.run代替os.system增加安全性和控制性
    import subprocess
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    running = False
    thread.join()
    if result.returncode == 0:
        sys.exit(0)
    else:
        sys.exit(result.returncode)
