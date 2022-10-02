#!/bin/usr/python3
""" Module Command Controller """

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ implements command line functionality """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quits the program """
        return True

    def do_EOF(self, arg):
        """ exits command line """
        return True

    def emptyline(self):
        """ handles an empty line by doing nothing """
        pass

    def do_create(self, arg):
        """ creates new instance of Base Model, saves to JSON,
            prints id """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        if len(arg) > 1:
            print("** too many arguments **")
            return False
        if arg[0] != 'BaseModel':
            print('** class name missing **')
            return False
        new_obj = eval(str(args) + '()')
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """ prints str representation of an instance based
            on class name and id """
        arg = args.split()
        if len(args) < 1:
            print('** class name missing **')
            return False
        if arg[0] != 'BaseModel':
            print('** class name missing **')
            return False
        if len(arg) < 2:
            print('** instance id missing **')
            return False
        if len(arg) > 2:
            print('** too many arguments **')
            return False

    def do_destroy(self, arg):
        """ deletes an instance based on class name and id """
        arg = args.split()
        if len(args) < 1:
            print('** class name missing **')
            return False
        if arg[0] != 'BaseModel':
            print('** class name missing **')
            return False
        if len(arg) < 2:
            print('** instance id missing **')
            return False
        if len(arg) > 2:
            print('** too many arguments **')
            return False
            """    obj_search = list_args[0] + '.' + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    del obj_all[obj_search]
                    storage.save()    """

    def do_all(self, arg):
        """ prints str representation of all instances of the object """
        arg = args.split()
        if len(args) < 1:
            print('** class name missing **')
            return False
        if arg[0] != 'BaseModel':
            print('** class name missing **')
            return False
        if len(arg) < 2:
            print('** instance id missing **')
            return False
        if len(arg) > 2:
            print('** too many arguments **')
            return False

    def do_update(self, arg):
        """ updates an instance based on class name and id
            by adding or updating an attribute """
        arg = args.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        if arg[0] != 'BaseModel':
            print('** class name missing **')
            return False
        if len(arg) < 2:
            print('** instance id missing **')
            return False
        if len(arg) < 3:
            print('** attribute name missing **')
            return False
        if len(arg) < 4:
            print('** value missing **')
            return False
        if len(arg) > 4:
            print('** too many arguments **')
            return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
