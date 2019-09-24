# import random
#
#
# class GreetServer(object):
#     def __init__(self):
#         pass
#
#     def get_greet(self, name='NoName'):
#         lucky_number = random.randint(1, 100000)
#         return "Hello {}, this is your lucky number {}".format(name, lucky_number)
#
#
# if __name__ == '__main__':
#     k = GreetServer()
#     print(k.get_greet('royyana'))

import random
import os
import glob


class GreetServer(object):
    def __init__(self):
        pass

    def tes(self):
        return  "success"

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def do_create(self, filename, text):
        if filename is None or filename == "":
            return "Filename is not defined"
        try:
            with open(filename, 'x') as file:
                file.write(text)
                return "{} created".format(filename)
        except Exception as e:
            return e

    def do_read(self, filename):
        if filename is None or filename == "":
            return "Filename is not defined"
        try:
            with open(filename, 'r') as file:
                return file.read()
        except Exception as e:
            return e

    def do_update(self, filename, text):
        if filename is None or filename == "":
            return "Filename is not defined"
        try:
            with open(filename, 'x') as file:
                file.write(text)
                return "{} updated".format(filename)
        except Exception as e:
            return e

    def do_delete(self, filename):
        if filename is None or filename == "":
            return "Filename is not defined"
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
    k = GreetServer()
    print(k.get_greet('royyana'))