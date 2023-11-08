#!/usr/bin/python3
"""
Implements a class which act as the entry point of command interpreter.

The class obey the following conventions:

1. End of file on input exits the command interpreter. (It calls the method
   'do_EOF')
2. The command 'quit' exits the program. (It calls the method 'do_quit')
3. The command 'create' creates a new instance of BaseModel, saves it
   (to the JSON file) and prints the 'id'. (It calls the method 'do_create').
   Ex: `create BaseModel`
4. Typing an empty line does not execute anything. (Actually, it calls the
   method `emptyline')
5. The command 'show' prints the string representation of an instance based
   on the class name and 'id'. (It calls the method 'do_show').
   Ex: `show BaseModel 1234-1234-1234`
6. The command 'destroy' deletes an instance based on the class name and id
   (save the change into the JSON file). (It calls the method 'do_destroy').
   Ex: `destroy BaseModel 1234-1234-1234`
7. The command 'all' prints all string representation of all instances based
   or not on the class name. (It calls the method 'do_all').
   Ex: `all BaseModel` or `all`
8. The command 'update' updates an instance based on the class name and id by
   adding or updating attribute (save the change into the JSON file). (It
   calls the method 'do_update')
   Ex: `update BaseModel 1234-1234-1234 email "aibnb@mail.com"`

"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage


PROMPT = '(hbnb) '
MISSING_CLASS_NAME = '** class name missing **'
NO_CLASS = "** class doesn't exist **"
MISSING_INST_ID = '** instance id missing **'
INST_NOT_FOUND = '** no instance found **'
classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter which inherits from cmd module
    """
    prompt = PROMPT

    def do_EOF(self, arg):
        """Handles EOF"""
        print()
        return True

    def do_quit(self, arg):
        """Exits the command intepreter"""
        return True

    def help_quit(self):
        """Displays quit command info"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = custom_parser(arg)
        if len(args) == 0:
            print(MISSING_CLASS_NAME)
        elif args[0] not in classes:
            print(NO_CLASS)
        else:
            new_id = eval(args[0])().id
            print(f'{new_id}')
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        all_obj = storage.all()
        args = custom_parser(arg)
        if len(args) == 0:
            print(MISSING_CLASS_NAME)
        elif args[0] not in classes:
            print(NO_CLASS)
        elif len(args) < 2:
            print(MISSING_INST_ID)
        elif "{}.{}".format(args[0], args[1]) not in all_obj:
            print(INST_NOT_FOUND)
        else:
            print(all_obj["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        all_obj = storage.all()
        args = custom_parser(arg)
        if len(args) == 0:
            print(MISSING_CLASS_NAME)
        elif args[0] not in classes:
            print(NO_CLASS)
        elif len(args) < 2:
            print(MISSING_INST_ID)
        elif "{}.{}".format(args[0], args[1]) not in all_obj.keys():
            print(INST_NOT_FOUND)
        else:
            del all_obj["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name
        """
        args = custom_parser(arg)
        if (len(args) > 0):
            class_name = args[0]
            if class_name not in classes:
                print(NO_CLASS)
                return
            object_list = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name
            ]
        else:
            object_list = [str(obj) for obj in storage.all().values()]

        print(object_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        pass

    def emptyline(self):
        """Does not execute anything"""
        pass


def custom_parser(arg):
    """
    Parse command arguments to a list
    """
    curly_match = re.search(r"\{(.*?)\}", arg)
    bracket_match = re.search(r"\[(.*?)\]", arg)

    if curly_match is None:
        if bracket_match is None:
            return [item.strip(",") for item in split(arg)]
        else:
            tokens = split(arg[:bracket_match.span()[0]])
            result_list = [item.strip(",") for item in tokens]
            result_list.append(bracket_match.group())
            return result_list
    else:
        tokens = split(arg[:curly_match.span()[0]])
        result_list = [item.strip(",") for item in tokens]
        result_list.append(curly_match.group())
        return result_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
