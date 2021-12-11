"""
    pyed - a simple 1 line based text editor

    This is an extremely simple (and broken)
    text editor, mainly made as a fun project 
    and a spiritual successor to worder.py, 
    which was a much more user friendly, albeit
    limited editor that was written in Python 2.
"""

import os

def write(filename,contents):
    f = open(filename,"a")
    f.write(contents)
    if f:
        print(f'{filename}: {os.path.getsize(filename)}')
        f.close()
    else:
        print("!")

def read(filename,mode):
    f = open(filename,"r")
    if mode == "p":
        print(f.read())
        f.close()
    elif mode == "n":
        # line numbers mode
        # do a little loop to get line numbers, then output them
        lines = sum(
            1 for line in f
        )
        print(lines)
        for i in range(lines):
            print(f.readline(i) + " " + f.readlines(i))
        f.close()
    else:
        print("?")

def removeLine(filename,line):
    f = open(filename,"a")
    f.writelines(line,"")
    if f:
        pass
    else:
        print("!")

def main():
    running = True
    while running:
        k = input()
        
        if k == "q":
            quit()

        else:
            sk = k.split(" ")
            try:
                if sk[0] == "w":
                    getInput = True

                    while getInput:
                        wInput = input()
                        if wInput != ".":
                            write(sk[1],f'\n{wInput}')
                        else:
                            getInput = False
                
                elif sk[0] == "p":
                    read(sk[1],"p")
                
                elif sk[0] == "n":
                    read(sk[1],"n")

                elif sk[0] == "r":
                    if sk[2]:
                        removeLine(sk[1],sk[2])
                    else:
                        print("!")
                
            except:
                print("?")

if __name__ == "__main__":
    main()