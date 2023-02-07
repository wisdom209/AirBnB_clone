#!/usr/bin/python3
"""Defines the console.py module with class HBNBCommand"""
import cmd


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

if __name__ == "__main__":
        HBNBCommand().cmdloop()
