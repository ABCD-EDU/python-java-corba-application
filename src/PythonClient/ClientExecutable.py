import CORBA, WordUnscramblerApp, CosNaming

def main(args):
    orb = CORBA.ORB_init(args, CORBA.ORB_ID)
    print("----------------------")
    print("CLIENT STARTING...")
    print("----------------------")

    obj = orb.resolve_initial_references("NameService")
    rootContext = obj._narrow(CosNaming.NamingContext)

    if rootContext is None:
        print ("Failed to narrow the root naming context")
        sys.exit(1)

    name = [CosNaming.NameComponent("Hello", ""), ]
    try:
        obj = rootContext.resolve(name)
    except CosNaming.NamingContext.NotFound as ex:
        print ("Name not found")
        sys.exit(1)

    eo = obj._narrow(WordUnscramblerApp.WordUnscrambler)

    if eo is None:
        print ("Object reference is not an WordUnscramblerApp::WordUnscrambler")
        sys.exit(1)

    print(eo.logIn("hotdog"))

    print("----------------------")
    print("ORB DESTROYED")
    orb.destroy()


if __name__ == "__main__":
    import sys
    main(sys.argv)
    print("----------------------")
    print("CLIENT NOW EXITING...")
    print("----------------------")