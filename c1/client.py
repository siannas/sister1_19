import Pyro4
import base64
import json
import sys

namainstance = sys.argv[1] or "fileserver"
path = namainstance+"/"
namainstance = "server."+namainstance

switcher = {
    1: "create",
    2: "read",
    3: "update",
    4: "delete",
    5: "list"
}

def method_selector(tipe):
    method = "do_"+ switcher.get(tipe)
    # print(method)
    # print(type(tipe))
    method_to_call = getattr(f, method)

    if tipe == 1:
        filename = input("Nama File : ")
        text = input("Konten : ")
        print(method_to_call(filename, text))
    elif tipe == 2:
        filename = input("Nama File : ")
        print(method_to_call(filename))
    elif tipe == 3:
        filename = input("Nama File : ")
        text = input("Konten : ")
        print(method_to_call(filename, text))
    elif tipe == 4:
        filename = input("Nama File : ")
        print(method_to_call(filename))
    elif tipe == 5:
        directory = input("Direktori : ")
        print(method_to_call(directory))

def test_no_ns():
    uri = "PYRO:obj_27d7c59497c44c688319f7d8a4a95935@localhost:40549"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def test_with_ns():
    while True:
        key = input("\nSilahkan pilih:\n\t1 membuat file\n\t2 membaca file\n\t3 mengupdate file\n\t4 mendelete file\n\t5 melihat list files\n\t6 keluar\n> ")
        tipe = int(key)
        if not key or tipe < 1 or tipe > 6:
            print("masukan input yang tepat!")
        elif tipe == 6:
            break
        else:
            method_selector(tipe)

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    fserver.setPath(path)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    test_with_ns()
