#!/bin/usr/python3
""" Module Command Controller """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ implements command line functionality """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quits current shell """
        return True

    def do_EOF(self, arg):
        """ quits current shell """
        return True

    def emptyline(self):
        """ handles an empty line """
        pass

    def do_create(self, arg):
        """ creates new instance of Base Model, saves to JSON,
            prints id """
        pass

    def do_show(self, arg):
        """ prints str representation of an instance based
            on class name and id """
        pass

    def do_destroy(self, arg):
        """ deletes an instance based on class name and id """
        pass

    def do_all(self, arg):
        """ prints str representation of all instances on the class name """
        pass

    def do_update(self, arg):
        """ updates an instance based on class name and id
            by adding or updating an attribute """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
