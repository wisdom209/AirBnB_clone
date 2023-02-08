#!/usr/bin/python3
"""Defines the console.py module with class HBNBCommand"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class definition for HBNBCommand that inherits from Cmd class for
    to build line oriented command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit command to exit from the interprter"""
        return True

    def do_EOF(self, line):
        """ctrl+D use to kill the program and exit from the interpreter"""
        return True

    def emptyline(self):
        """returns nothing for emptyline + enter"""
        pass

    def do_create(self, class_name):
        "Creates a new BaseModel instance, saves and prints the ID"
        if class_name:
            if type(class_name) is BaseModel:
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
