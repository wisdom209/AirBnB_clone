#!/usr/bin/python3
"""Defines the console.py module with class HBNBCommand"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import helper_functions
import sys


class HBNBCommand(cmd.Cmd):
    """
    class definition for HBNBCommand that inherits from Cmd class for
    to build line oriented command interpreter
    """

    prompt = "(hbnb) "

    class_tuple = ("BaseModel", "User", "City", "State",
                   "Amenity", "Place", "Review")

    def default(self, line):
        """Override some error message"""
        show_regex = re.compile("(.*)\\.show\\(.*\\)")
        show_match = show_regex.match(line.strip())

        destroy_regex = re.compile("(.*)\\.destroy\\(.*\\)")
        destroy_match = destroy_regex.match(line.strip())

        update_regex = re.compile("(.*)\\.update\\(.*\\)")
        update_match = update_regex.match(line.strip())

        all_regex = re.compile("(.*)\\.all\\(\\)")
        all_match = all_regex.match(line.strip())

        match_list = [update_match, show_match, all_match, destroy_match]

        for i in match_list:
            if (i):
                class_name = i.group(1)
                if class_name not in self.class_tuple:
                    print("** class doesn't exist **")

    def do_help(self, arg):
        """help me"""
        if (not sys.stdin.isatty()):
            print()
        return super().do_help(arg)

    def do_quit(self, line):
        """quit command to exit from the interprter"""
        return True

    def do_EOF(self, line):
        """ctrl+D use to kill the program and exit from the interpreter"""
        print()
        return True

    def emptyline(self):
        """returns nothing for emptyline + enter"""
        pass

    def do_create(self, class_name):
        "Creates a new BaseModel instance, saves and prints the ID"

        if class_name:
            if class_name in self.class_tuple:
                my_model = eval(class_name + "()")
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        class_name = None
        instance_id = None
        args = None

        if (line and len(line) != 0):
            args = line.split()
            class_name = args[0]

            if (len(args) > 1):
                instance_id = args[1]

        if class_name:
            if class_name not in self.class_tuple:
                print("** class doesn't exist **")
            else:
                if not instance_id:
                    print("** instance id missing **")

                if instance_id:
                    if not helper_functions.show_instance(class_name,
                                                          instance_id):
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        class_name = None
        instance_id = None
        args = None

        if (line and len(line) != 0):
            args = line.split()
            class_name = args[0]

            if (len(args) > 1):
                instance_id = args[1]

        if class_name:
            if class_name not in self.class_tuple:
                print("** class doesn't exist **")
            else:
                if not instance_id:
                    print("** instance id missing **")

                if instance_id:
                    if not helper_functions.delete(class_name, instance_id):
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, class_name):
        """Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all."""
        if not class_name:
            print(helper_functions.get_all())
        elif class_name in self.class_tuple:
            print(helper_functions.get_all(class_name))
        else:
            print("** class doesn't exist **")

    def do_update(self, line, isDotUpdate=None):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'."""
        print("log:",line)
        class_name = None
        id = None
        attr_name = None
        attr_value = None
        old_line = line

        if isDotUpdate:
            line = re.sub(r'"\s+"', '_[*]_', line)
            line = re.sub(r"'\s+'", '_[*]_', line)
            line = re.sub(r"\"\s+'", '_[*]_', line)
            line = re.sub(r"'\s+\"", '_[*]_', line)

            args = line.split('_[*]_')
        else:
            args = line.split(" ")

        tot_args = len(args)

        for i in range(tot_args):
            if i == 0:
                class_name = args[0].strip().strip('\"').strip("\'")
            if i == 1:
                id = args[1].strip().strip('\"').strip("\'")
            if i == 2:
                attr_name = args[2].strip().strip('\"').strip("\'")
            if i == 3:
                # quoted_string_regex = re.compile('(\\s\".*?\"\\s?)')
                # match = quoted_string_regex.search(old_line)
                # if (match and isDotUpdate):
                #     attr_value = match.group(1)
                #     print("log:regexerr", attr_value)
                # else:
                attr_value = args[3].strip().strip('\"').strip("\'")

        if class_name:
            if class_name not in self.class_tuple:
                print("*** class doesn't exist ***")
            else:
                if id:
                    obj = FileStorage()
                    full_key = f"{class_name}.{id}"
                    
                    if full_key in obj.all().keys():
                        if not attr_name:
                            print("** attribute name is missing **")
                        else:
                            if not attr_value:
                                print("** value missing **")
                            else:
                                print("log:attr_value -", attr_value)
                                helper_functions.update_instance(
                                    class_name,
                                    id, attr_name, attr_value)
                    else:
                        print("** no instance found **")
                        return 0
                else:
                    print("** instance id missing **")
        else:
            print("*** class name is missing ***")

    def handle_common_actions(self, class_name, line):
        """Handle some repeated actions"""
        if line.strip() == ".all()":
            print(eval(class_name + ".all()"))
        elif line.strip() == ".count()":
            print(eval(class_name + ".count()"))
        elif line.strip().startswith(".show("):
            id = line.strip()[6:-1]
            if (id == ""):
                print("** instance id missing **")
            elif not getattr(eval(class_name), 'show')(class_name, id):
                print("** no instance found **")
        elif line.strip().startswith(".destroy("):
            id = line.strip()[9:-1]
            if (id == ""):
                print("** instance id missing **")
            elif not getattr(eval(class_name), 'destroy')(class_name, id):
                print("** no instance found **")
        elif line.strip().startswith(".update("):
            line = line.lstrip('.update(')[:-1]
            # match dict update
            dict_regex = re.compile("(.*?,\\s*?)(\\{.*?\\}$)|(\\{.*?\\},.+?)")
            dict_match = dict_regex.match(line)

            if (dict_match):
                for i in range(len(line)):
                    if line[i] == "}":
                        line = line[:i+1]

                line = line.split(", {")
                line[1] = "{" + line[1]
                is_value_dict = eval(f"{line[1]}")
                if (type(is_value_dict) is dict):
                    updated = None
                    for k, v in is_value_dict.items():
                        if (v != ""):
                            if type(v) is str:
                                v = v.strip()
                                if ' ' in v:
                                    v = f'"{v}"'
                            updated = f'"{class_name}" "{line[0]}" "{k}" "{v}"'
                            ret = self.do_update(updated, True)

                            if ret == 0:
                                break
                return 1

            line = line.split(",")

            quote_match = True
            for x in range(len(line)):
                if (x < 3):
                    quote_regex = re.compile('(^\'.+\'$)|(^\".+\"$)')
                    quote_match = quote_regex.match(line[x].strip(" "))
                    if not quote_match:
                        break

            if (line and (line[0] == "")):
                print("** instance id missing **")
            elif not quote_match:
                pass
            else:
                line.insert(0, f'"{class_name}"')
                line = " ".join(line)
                self.do_update(line, True)

    def do_Amenity(self, line):
        """print Amenities"""
        self.handle_common_actions("Amenity", line)

    def do_BaseModel(self, line):
        """print BaseModels"""
        self.handle_common_actions("BaseModel", line)

    def do_City(self, line):
        """print Cities"""
        self.handle_common_actions("City", line)

    def do_Place(self, line):
        """print Places"""
        self.handle_common_actions("Place", line)

    def do_Review(self, line):
        """print Reviews"""
        self.handle_common_actions("Review", line)

    def do_State(self, line):
        """print States"""
        self.handle_common_actions("State", line)

    def do_User(self, line):
        """count Users"""
        self.handle_common_actions("User", line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
