# 9322-finGrp2

## Running the Program:
### How to run Java Server
1. Go to `out/production/9322-fingrp2` using your terminal (`<path-to-out/production>`)
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
from project folder `cd src/JavaServer` then `javac WordUnscramblerApp/*.java server/*.java -d <path-to-out/production>`

#### Java Client

from project folder `cd src/JavaClient` then `javac *.java WordUnscramblerApp/*.java model/*.java controllers/*.java -d <path-to-out/production>`
