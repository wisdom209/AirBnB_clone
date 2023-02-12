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

        # Get the regex for class_name.show(args)
        # Get the regex for class_name.destroy(args)
        # Get the regex for class_name.update(args)
        # Get the regex for class_name.all(args)
        show_regex = re.compile("(.*)\\.show\\(.*\\)")
        destroy_regex = re.compile("(.*)\\.destroy\\(.*\\)")
        update_regex = re.compile("(.*)\\.update\\(.*\\)")
        all_regex = re.compile("(.*)\\.all\\(\\)")

        # match the regex with the line
        show_match = show_regex.match(line.strip())
        destroy_match = destroy_regex.match(line.strip())
        update_match = update_regex.match(line.strip())
        all_match = all_regex.match(line.strip())

        match_list = [update_match, show_match, all_match, destroy_match]

        # check if class exists
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
        """Prints the string representation of an instance"""

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
        class_name = None
        id = None
        attr_name = None
        attr_value = None
        quoted_attr_value = None
        do_update = 1
        args = []

        if isDotUpdate:
            args = line.split(",")
        else:
            arg_list = helper_functions.get_do_update_arg_list(
                do_update, isDotUpdate, line)
            args, do_update, quoted_attr_value = arg_list

        param_list = helper_functions.get_needed_params_for_do_update(
            args, quoted_attr_value, do_update)
        class_name, id, attr_name, attr_value, do_update = param_list

        if class_name:
            if class_name not in self.class_tuple:
                print("** class doesn't exist **")
            else:
                if id:
                    obj = FileStorage()
                    full_key = f"{class_name}.{id}"
                    if full_key in obj.all().keys():
                        if not attr_name:
                            print("** attribute name missing **")
                        else:
                            if not attr_value:
                                print("** value missing **")
                            else:
                                if do_update:
                                    helper_functions.update_instance(
                                        class_name,
                                        id, attr_name, attr_value)
                    else:
                        print("** no instance found **")
                        return 0
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def update_with_a_dict(self, line, class_name):
        """Update an Object using a whole dict"""
        for i in range(len(line)):
            if line[i] == "}":
                line = line[:i+1]

        line = line.split(", {")
        if (line and len(line) >= 2):
            line[1] = "{" + line[1]
        try:
            is_value_dict = eval(f"{line[1]}")
        except Exception:
            is_value_dict = None

        if (type(is_value_dict) is dict):
            updated = None
            for k, v in is_value_dict.items():
                if (v != ""):
                    if type(v) is str:
                        v = v.strip()
                        v = f'"{v}"'
                    instance_id = line[0].strip().strip("\'").strip('"')
                    updated = f'{class_name} {instance_id} {k} {v}'
                    ret = self.do_update(updated, False)
                    if ret == 0:
                        break

    def check_dotUpdate_quotes(self, line):
        """Check parameters in dot updates are quoted"""
        quote_match = True
        for x in range(len(line)):
            if (x < 2):
                quote_regex = re.compile('(^\'.+\'$)|(^\".+\"$)')
                quote_match = quote_regex.match(line[x].strip())
                if not quote_match:
                    break
        return quote_match

    def handle_common_actions(self, class_name, line):
        """Handle some repeated actions"""
        if line.strip() == ".all()":
            print(eval(class_name + ".all()"))
        elif line.strip() == ".count()":
            print(eval(class_name + ".count()"))
        elif (line.strip() == ".show()" or
              line.strip().startswith(".show('") or
              line.strip().startswith('.show("')) and \
                line.strip().endswith(")"):
            id = line.strip()[6:-1]
            if (id == "" or not id.strip("'") or not id.strip('\"')
                    or line.strip() == ".show()"):
                print("** instance id missing **")
            elif not self.check_dotUpdate_quotes([id.strip()]) \
                    or len(id.split(", ")) > 1:
                pass
            elif not getattr(eval(class_name), 'show')(class_name, id):
                print("** no instance found **")
        elif (line.strip() == ".destroy()" or
              line.strip().startswith(".destroy('") or
              line.strip().startswith('.destroy("')) and \
                line.strip().endswith(')'):
            id = line.strip()[9:-1]

            if (id == "" or not id.strip("'") or not id.strip('\"')
                    or line.strip == ".destroy()"):
                print("** instance id missing **")
            elif not self.check_dotUpdate_quotes([id.strip()]) \
                    or len(id.split(", ")) > 1:
                pass
            elif not getattr(eval(class_name), 'destroy')(class_name, id):
                print("** no instance found **")
        elif line.strip().startswith(".update(") and \
                line.strip().endswith(')'):
            line = line.lstrip('.update(')[:-1]
            # match dict update
            dict_regex = re.compile(
                r"([\"\'].*?[\"\'],\s*?)(\{.*?\}$)|(\{.*?\},\s.+?)")
            dict_regex_miss_id = re.compile(r"(\{.*\})")
            dict_match = dict_regex.match(line.strip())
            dict_no_id = dict_regex_miss_id.match(line.strip())

            if (dict_match):
                # TODO: handle missing instance id
                self.update_with_a_dict(line, class_name)
            elif dict_no_id and type(eval(f"{dict_no_id.group(1)}")) is dict:
                print("** instance id missing **")
            else:
                line = line.split(", ")
                is_dotUpdate_well_quoted = self.check_dotUpdate_quotes(line)

                if (line and (line[0] == "")):
                    print("** instance id missing **")
                elif not is_dotUpdate_well_quoted:
                    pass
                else:
                    line.insert(0, f'"{class_name}"')
                    line = ",".join(line)
                    self.do_update(line, True)

    def do_Amenity(self, line):
        """print Amenities"""
        self.handle_common_actions("Amenity", line)

    def do_BaseModel(self, line):
        """print BaseModel"""
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
