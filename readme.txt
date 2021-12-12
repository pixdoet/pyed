_____PYED MANUAL_____

This is the manual for PyED.

_____CONTENTS_____
1. Installation
2. Using PyED
3. Troubleshooting
4. Contact
5. Copyright and licenses

_____1. INSTALLATION______
There is currently only one way to install PyED officially, and that is cloning the repository from Github.
To install PyED, run the following command:
    
    git clone https://github.com/pixdoet/pyed.git

To update PyED when possible, run the following command in the directory you intent to use PyED:

    git pull origin main

To remove PyED, run the following command in the PyED directory:

    rm -rf *

_____2. Using PyED_____

2.1 COMMANDS
Note: Text written in square brackets[] are required arguments and should always be there. Text written in curly brackets{} are optional arguments and can be applied by choice.

There are currently 4 commands in PyED. They are:
    p: Prints out contents of a file. Usage: p [filename]
    n: Prints out contents of a file with line numbers in front. Usage: n [filename]
    w: Writes contents into a file. Usage: w [filename]
       When using w, the editor will switch to editing mode. Type a single full stop (.) to exit out of edit mode. When exited, the editor will print a single asterisk (*)
    q: Quits the program. Usage: q

2.2 STATUS CODES
There are currently 3 status codes in PyED. They are:
    *: OK
    !: Program error/Non-user created error. This could mean corrupted files, unreadable files and/or internal program errors.
    ?: User generated error. This could mean that the file was not found, or the input is invalid.

_____3. TROUBLESHOOTING_____
There is nothing to troubleshoot.

_____4. CONTACT_____
You can contact the developer on Github(pixdoet), Discord(maybeimawok#6686) or Email(thefkbk@gmail.com)

_____5. COPYRIGHT AND LICENSES______
This software is licensed under the Apache 2.0 license. See COPYING in this folder.