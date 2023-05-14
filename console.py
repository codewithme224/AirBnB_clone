#!/usr/bin/python3
"""Module for console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        objects = {
                "BaseModel": BaseModel(), "User": User(),
                "City": City(), "State": State(),
                "Amenity": Amenity, "Place": Place(),
                "Review": Review()
                }
        cap_arg = arg.capitalize()

        if not arg:
            print("** class name missing **")
        elif cap_arg not in objects:
            print("** class doesn't exist **")
        else:
            new = objects[cap_arg]
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

        objects = {
                "BaseModel": BaseModel(), "User": User(),
                "City": City(), "State": State(),
                "Amenity": Amenity, "Place": Place(),
                "Review": Review()
                }
        cap_args = arg.capitalize()

        if not arg:
            print("** class name missing **")
        else:
            args = cap_args.split()
            if args[0] not in objects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = f'{args[0]}.{args[1]}'
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        objects = {
                "BaseModel": BaseModel(), "User": User(),
                "City": City(), "State": State(),
                "Amenity": Amenity, "Place": Place(),
                "Review": Review()
                }
        cap_arg = arg.capitalize()
        if not arg:
            print("** class name missing **")
        else:
            args = cap_arg.split()
            if args[0] not in objects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = f'{args[0]}.{args[1]}'
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        objects = {
                "BaseModel": BaseModel(), "User": User(),
                "City": City(), "State": State(),
                "Amenity": Amenity, "Place": Place(),
                "Review": Review()
                }
        cap_arg = arg.capitalize()
        if not arg:
            for key, value in models.storage.all().items():
                print(value)
        else:
            args = cap_arg.split()
            if args[0] not in objects:
                print("** class doesn't exist **")
            else:
                for key, value in models.storage.all().items():
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        objects = {
                "BaseModel": BaseModel(), "User": User(),
                "City": City(), "State": State(),
                "Amenity": Amenity, "Place": Place(),
                "Review": Review()
                }
        cap_arg = arg.capitalize()
        if not arg:
            print("** class name missing **")
        else:
            args = cap_arg.split()
            if args[0] not in objects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = f'{args[0]}.{args[1]}'
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[key], args[2], args[3])
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
