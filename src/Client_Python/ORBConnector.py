import CORBA 
import WordUnscramblerApp
import CosNaming
import sys

class ORBConnector():
    def __init__(self, args):
        self.readConfig()
        if len(args) > 1:
            self.orb = CORBA.ORB_init(args, CORBA.ORB_ID)
        elif len(self.params) > 1:
            self.orb = CORBA.ORB_init(self.params, CORBA.ORB_ID)

        self.obj = self.orb.resolve_initial_references("NameService")
        self.rootContext = self.obj._narrow(CosNaming.NamingContext)

        if self.rootContext is None:
            print ("Failed to narrow the root naming context")
            sys.exit(1)

        self.name = [CosNaming.NameComponent("WordGame", ""), ]
        try:
            self.obj = self.rootContext.resolve(self.name)
        except CosNaming.NamingContext.NotFound as ex:
            print ("Name not found")
            sys.exit(1)

        self.eo = self.obj._narrow(WordUnscramblerApp.WordUnscrambler)

        if self.eo is None:
            print ("Object reference is not an WordUnscramblerApp::WordUnscrambler")
            sys.exit(1)

    def readConfig(self):
        self.params = []
        host = ''
        port = ''
        with open('../../.config') as lines:
            for line in lines:
                line = line.strip()
                cfg = line.split('=')[1]
                if 'host' in line:
                    host = cfg
                if 'port' in line:
                    port = cfg

        self.params = ['PythonClient.py', '-ORBInitRef', 'NameService=corbaname::{host}:{port}'.format(host=host, port=port)]

    def getEO(self):
        return self.eo

    def close(self):
        self.orb.destroy()