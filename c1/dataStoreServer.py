from fileDataStore import *
import Pyro4
import sys

def start():
    # ds = FileDataStore()
    with Pyro4.Daemon(host="localhost") as daemon:
        x_fileserver = Pyro4.expose(FileDataStore)
        s_uri = daemon.register(x_fileserver)
        with Pyro4.locateNS("localhost", 7777) as ns:
            ns.register("datastore", s_uri)
            daemon.requestLoop()

if __name__=='__main__':
    start()