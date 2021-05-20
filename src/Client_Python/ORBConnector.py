import CORBA 
import WordUnscramblerApp
import CosNaming
import sys

class ORBConnector():
    def __init__(self, args):
        self.orb = CORBA.ORB_init(args, CORBA.ORB_ID)
        print("----------------------")
        print("CLIENT STARTING...")
        print("----------------------")

        self.obj = self.orb.resolve_initial_references("NameService")
        self.rootContext = self.obj._narrow(CosNaming.NamingContext)

        if self.rootContext is None:
            print ("Failed to narrow the root naming context")
            sys.exit(1)

        self.name = [CosNaming.NameComponent("Hello", ""), ]
        try:
            self.obj = self.rootContext.resolve(self.name)
        except CosNaming.NamingContext.NotFound as ex:
            print ("Name not found")
            sys.exit(1)

        self.eo = self.obj._narrow(WordUnscramblerApp.WordUnscrambler)

        if self.eo is None:
            print ("Object reference is not an WordUnscramblerApp::WordUnscrambler")
            sys.exit(1)

    def getEO(self):
        return self.eo

    def close(self):
        self.orb.destroy()