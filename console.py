#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements
the command interpreter.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.

    args:
    prompt: str that will be showed to the user

    Methods:
        do_quit(self, arg): Quit command to exit the program
        do_EOF(self, arg): Quit command to exit the program when receive EOF
        emptyline(self): Empty line + ENTER shouldn't execute anything
        help_quit(self): Help message for the quit command
        do_create(self, arg): Creates a new instance of any available model
        do_show(self, arg): Prints the string representation of an instance
        do_destroy(self, arg): Deletes an instance based on name and id
        do_all(self, arg): Prints all string representation of all instances
        do_update(self, arg): Updates an instance based on name and id
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review()
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")

    def default(self, arg):
        """Handle any command that is not defined"""
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        if "." in arg:
            args = arg.split(".")
            class_name = args[0]
            method_name = args[1].split("(")[0]
            if class_name in self.classes and method_name in methods:
                if "(" in args[1] and ")" in args[1]:
                    id_arg = args[1].split("(")[1].split(")")[0]
                    methods[method_name](class_name + " " + id_arg)
                else:
                    methods[method_name](class_name)
            else:
                print("** Unknown syntax: {} **".format(arg))
        else:
            print("** Unknown syntax: {} **".format(arg))

    def do_create(self, arg):
        """
        Creates a new instance of any available model,
        and saves it (to the JSON file) and prints the id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_obj = self.classes[args[0]]
            class_obj.save()
            print(class_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        args = shlex.split(arg)
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.items()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if arg[0].endswith('.all'):
                class_name = arg[0].split(".")[0]
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(class_name)]
                strs = [str(obj) for obj in class_objs]
                print(strs)
            else:
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(arg[0])]
                strs = [str(obj) for obj in class_objs]
                print(strs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** dictionary representation missing **")
            else:
                obj = all_objs[key]
                try:
                    data = eval(args[2])
                except (SyntaxError, NameError):
                    print("** invalid dictionary representation **")
                    return
                if isinstance(data, dict):
                    for k, v in data.items():
                        setattr(obj, k, v)
                    obj.save()
                else:
                    print("** invalid dictionary representation **")

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            count = len(
                [obj for key, obj in all_objs.items()
                 if key.startswith(arg[0])]
                        )
            print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
