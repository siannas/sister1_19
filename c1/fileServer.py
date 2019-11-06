import random
import os
import glob

class FileServer(object):
    def __init__(self):
        pass

    def tes(self):
        return  "success"

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def setPath(self, path):
        self.path = path
        try:
            os.mkdir(path)
        except Exception as e:
            print("Folder Exist")
        print(path)

    def do_create(self, filename, text):
        filename = self.path+filename
        if filename is None or filename == "":
            return "Nama File tidak terdefinisi"
        try:
            with open(filename, 'x') as file:
                file.write(text)
                return "{} created".format(filename)
        except Exception as e:
            return e

    def do_read(self, filename):
        filename = self.path + filename
        if filename is None or filename == "":
            return "Nama File tidak terdefinisi"
        try:
            with open(filename, 'r') as file:
                return file.read()
        except Exception as e:
            return e

    def do_update(self, filename, text):
        filename = self.path + filename
        if filename is None or filename == "":
            return "Nama File tidak terdefinisi"
        print("filename is will be updated")
        try:
            with open(filename, "r+") as f:
                f.seek(0)  # rewind
                f.write(text)
                return "{} updated".format(filename)
        except Exception as e:
            return e

    def do_delete(self, filename):
        filename = self.path + filename
        if filename is None or filename == "":
            return "Nama File tidak terdefinisi"
        try:
            os.remove(filename)
            return "{} deleted".format(filename)
        except Exception as e:
            return e

    def do_list(self, directory):
        try:
            files = [f for f in glob.glob(directory + "**/*", recursive=True)]
            list_files = "\nFile Lists:"
            for file in files:
                list_files += "\n"+file

            return list_files
        except Exception as e:
            return e


if __name__ == '__main__':
    k = FileServer()
    k.do_update("tes.txt", "asoy")
