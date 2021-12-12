"""
    pyed - a simple 1 line based text editor

    Manual: readme.txt
    Copyright 2021 Ian Hiew

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import os

def write(filename,contents):
    f = open(filename,"a")
    f.write(contents)
    if f:
        print(f'{filename}: {os.path.getsize(filename)}')
        print("*")
        f.close()
    else:
        print("!")

def read(filename,mode):
    f = open(filename,"r")
    if mode == "p":
        print(f.read())
        print("*")
        f.close()
    elif mode == "n":
        # line numbers mode
        # do a little loop to get line numbers, then output them
        lines = sum(
            1 for lines in f
        )
        print(lines)
        for i in range(lines):
            print(f.readline(i) + " " + f.readlines(i))
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
                            print("*")
                
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
    print("*")
    main()