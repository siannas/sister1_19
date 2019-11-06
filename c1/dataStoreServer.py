import Pyro4
import sys

@Pyro4.expose
class DataStore(object):
    def __init__(self):
        self.c_server = []
        with Pyro4.locateNS("localhost", 7777) as ns:
            for server, server_uri in ns.list(prefix="server").items():
                print("found server", server)
                self.c_server.append(server)

    @property
    def checkChild(self):
        for i in range(len(self.c_server)):
            print(self.c_server[i])

    @property
    def syncChild(self):
        del self.c_server[:]
        with Pyro4.locateNS("localhost", 7777) as ns:
            for server, server_uri in ns.list(prefix="server").items():
                print("found server", server)
                self.c_server.append(server)

    @property
    def createAll(self):
        filename = "asoy.txt"
        text = "sas"
        serverku = self.c_server
        for i in range(len(serverku)):
            path = serverku[i].split('.')[1]+"/"
            print(path)
            uri = "PYRONAME:{}@localhost:7777".format(serverku[i])
            fs = Pyro4.Proxy(uri)
            fs.setPath(path)
            fs.do_create(filename, text)

    @property
    def tesaja(self):
        print("haloo")

def start():
    ds = DataStore()
    with Pyro4.Daemon() as daemon:
        s_uri = daemon.register(ds)
        with Pyro4.locateNS("localhost", 7777) as ns:
            ns.register("datastore", s_uri)
        daemon.requestLoop()

if __name__=='__main__':
    start()