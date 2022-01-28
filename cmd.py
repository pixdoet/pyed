"""
    cmd.py for parsing individual commands sent to STDIN

    ©2021 Ian Hiew. All rights reserved
"""
import os

class Commands():    
    def edit(filename,contents):
        f = open(filename,"w")
        f.write(contents)
        if f:
            m = os.path.getsize(filename)
            return m

    def read(filename):
        f = open(filename,"r")
        a = f.read()
        return a
    
    def quit():
        quit()
#!/usr/bin/python3
print ("Hello world")
q