#!/usr/bin/python3
"""Defines the console.py module with class HBNBCommand"""
import cmd
import copy
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    class definition for HBNBCommand that inherits from Cmd class for
    to build line oriented command interpreter
    """

    prompt = "(hbnb) "

    class_tuple = ("BaseModel", "User", "City", "State",
                   "Amenity", "Place", "Review")

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
                    obj = FileStorage()
                    full_key = f"{class_name}.{instance_id}"

                    if full_key in obj.all().keys():
                        new_obj_dict = copy.deepcopy(obj.all())
                        for value in new_obj_dict.values():
                            if '__class__' in value.__dict__.keys():
                                del value.__dict__['__class__']
                        print(new_obj_dict[full_key])
                    else:
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
                    obj = FileStorage()
                    full_key = f"{class_name}.{instance_id}"

                    if full_key in obj.all().keys():
                        del obj.all()[full_key]
                        f = FileStorage()
                        f.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, class_name):
        """Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all."""
        if not class_name:
            obj = FileStorage()
            new_obj_dict = copy.deepcopy(obj.all())
            for value in new_obj_dict.values():
                if '__class__' in value.__dict__.keys():
                    del value.__dict__['__class__']
            obj_dict = [str(x) for x in new_obj_dict.values()]
            print(obj_dict)
        elif class_name in self.class_tuple:
            obj = FileStorage()
            new_obj_dict = copy.deepcopy(obj.all())

            new_obj_dict = {
                k: v for k, v in new_obj_dict.items()
                if k.startswith(class_name)}

            for value in new_obj_dict.values():
                if '__class__' in value.__dict__.keys():
                    del value.__dict__['__class__']
            obj_dict = [str(x) for x in new_obj_dict.values()]
            print(obj_dict)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'."""
        class_name = None
        id = None
        attr_name = None
        attr_value = None
        args = line.split()
        tot_args = len(args)

        for i in range(tot_args):
            if i == 0:
                class_name = args[0]
            if i == 1:
                id = args[1]
            if i == 2:
                attr_name = args[2]
            if i == 3:
                attr_value = args[3]

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
                                obj = FileStorage()
                                obj_to_update = obj.all()[full_key]
                                add_val = attr_value
                                try:
                                    add_val = eval(attr_value)
                                except Exception:
                                    pass
                                obj_to_update.__dict__[
                                    attr_name] = add_val
                                obj.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("*** class name is missing ***")

    def do_User(self, line):
        """count Users"""
        if line.strip() == ".all()":
            print(User.all())
        elif line.strip() == ".count()":
            print(User.count())

    def do_State(self, line):
        """print States"""
        if line.strip() == ".all()":
            print(State.all())
        elif line.strip() == ".count()":
            print(State.count())

    def do_Amenity(self, line):
        """print Amenities"""
        if line.strip() == ".all()":
            print(Amenity.all())
        elif line.strip() == ".count()":
            print(Amenity.count())

    def do_City(self, line):
        """print Cities"""
        if line.strip() == ".all()":
            print(City.all())
        elif line.strip() == ".count()":
            print(City.count())

    def do_Place(self, line):
        """print Places"""
        if line.strip() == ".all()":
            print(Place.all())
        elif line.strip() == ".count()":
            print(Place.count())

    def do_Review(self, line):
        """print Reviews"""
        if line.strip() == ".all()":
            print(Review.all())
        elif line.strip() == ".count()":
            print(Review.count())

    def do_BaseModel(self, line):
        """print BaseModels"""
        if line.strip() == ".all()":
            print(BaseModel.all())
        elif line.strip() == ".count()":
            print(BaseModel.count())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
