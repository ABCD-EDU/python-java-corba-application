# 9322-finGrp2

## Running the Program:
### How to run Java Server
1. Go to `out/production/9322-fingrp2` using your terminal (`<path-to-out/production/9322-fingrp2>`)
2. Start the ORB by typing in `orbd -ORBInitialPort 1050`
3. Start the JavaServer by typing in `java server.JavaServer -ORBInitialPort 1050 -ORBInitialHost localhost` or  `start java server.JavaServer -ORBInitialPort 1050 -ORBInitialHost localhost`
4. Soon after starting the server, the terminal will ask for a path leading to the text file to be used by the game.
5. Input the path of words.txt from the bin folder and press enter.


### How to run Java Client
1. Go to `out/production/9322-fingrp2` using your terminal (`cd path`)
2. Start the JavaClient by typing in `java ClientExecutable -ORBInitialPort 1050 -ORBInitialHost localhost` or `start java ClientExecutable -ORBInitialPort 1050 -ORBInitialHost localhost`
3. Press enter in the terminal.

## Compiling the Project
#### Java Server
from project folder `cd src/JavaServer` then `javac WordUnscramblerApp/*.java server/*.java -d <path-to-out/production/9322-fingrp2>`

#### Java Client

from project folder `cd src/JavaClient` then `javac *.java WordUnscramblerApp/*.java model/*.java controllers/*.java -d <path-to-out/production/9322-fingrp2>`

## Python Client

### Technologies used

The group used Python 2.7 as the programming language for the non-Java client and omniORBpy 4.2.0 as the CORBA Object Request Broker of choice. The group decided to use Python 2.7 mainly because it is the programming language and version supported by omniORBpy 4.2.0, which has detailed and easy-to-understand documentation and is easy to use compared to other object request brokers other programming languages offer.

### Set-up

    Download the appropriate version  of Python 2.7.0 from https://www.python.org/downloads/release/python-270/ and 
    omniORBpy from https://sourceforge.net/projects/omniorb/files/omniORBpy/omniORBpy-4.2.0/ according to your system’s specifications.

    The group recommends that if your system runs windows 10 64-bit then download the Windows X86-64 MSI Installer (2.7.0) [1] (sig) file to install Python 2.7.0 in your machine if other installers do not work.

Download the respective omniORBpy version according to your machine’s architecture. Unzip the downloaded file to your desired directory.

    Add the following variable to your system’s user environment variable:
    <omniorbpy-path>\bin\x86_win32

    (Where the <omniorbpy-path> environment variable is the root of your omniORB folder.)

Then add Python27 to your system’s Path environment variable. By default, Python 2.7.0 will be installed in your machine’s C:\Python27 directory.

### Generating the python stubs 

    To create the stubs, we enter the following in the command line: 

    omniidl -bpython <path-to-idl>
    (Where FILENAME is the idl’s file name)

This will generate two directories and one file. In our case, they are: WordUnscrambler, WordUnscramblerApp_POA, and WordUnscramblerApp_idl.py. Move the directory, WordUnscrambler, and the file WordUnscrmblerApp_idl.py to the same directory as to where the python’s client executable is going to be located. The WordUnscramblerApp_POA directory is only used for corba python servers, which we do not need.
