import Pyro4
import sys
import random
import os
import glob

class FileDataStore(object):
    def __init__(self):
        self.c_server = []
        with Pyro4.locateNS("localhost", 7777) as ns:
            for server, server_uri in ns.list(prefix="server").items():
                print("found server", server)
                self.c_server.append(server)

    def checkChild(self):
        for i in range(len(self.c_server)):
            print(self.c_server[i])

    def syncChild(self):
        del self.c_server[:]
        with Pyro4.locateNS("localhost", 7777) as ns:
            for server, server_uri in ns.list(prefix="server").items():
                print("found server", server)
                self.c_server.append(server)

    def createAll(self, filename, text):
        # filename = "asoy.txt"
        # text = "sas"
        serverku = self.c_server
        for i in range(len(serverku)):
            path = serverku[i].split('.')[1]+"/"
            print(path)
            uri = "PYRONAME:{}@localhost:7777".format(serverku[i])
            fs = Pyro4.Proxy(uri)
            fs.setPath(path)
            fs.do_create(filename, text)

    def updateAll(self, filename, text):
        serverku = self.c_server
        for i in range(len(serverku)):
            path = serverku[i].split('.')[1]+"/"
            print(path)
            uri = "PYRONAME:{}@localhost:7777".format(serverku[i])
            fs = Pyro4.Proxy(uri)
            fs.setPath(path)
            fs.do_update(filename, text)

    def deleteAll(self, filename):
        serverku = self.c_server
        for i in range(len(serverku)):
            path = serverku[i].split('.')[1]+"/"
            print(path)
            uri = "PYRONAME:{}@localhost:7777".format(serverku[i])
            fs = Pyro4.Proxy(uri)
            fs.setPath(path)
            fs.do_delete(filename)

    def tesaja(self):
        print("haloo")

if __name__ == '__main__':
    k = FileServer()
    k.do_update("tes.txt", "asoy")
