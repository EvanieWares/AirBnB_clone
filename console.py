#!/usr/bin/python3
"""Implements the HBNB console"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


PROMPT = '(hbnb) '
CLASS_NAME_MISSING = '** class name missing **'
NO_CLASS = "** class doesn't exist **"
INST_ID_MISSING = '** instance id missing **'
INST_NOT_FOUND = '** no instance found **'
ATTR_NAME_MISSING = '** attribute name missing **'
ATTR_VALUE_MISSING = '** value missing **'
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
        """EOF signal to exit the program."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = custom_parser(arg)
        if len(args) == 0:
            print(CLASS_NAME_MISSING)
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
            print(CLASS_NAME_MISSING)
        elif args[0] not in classes:
            print(NO_CLASS)
        elif len(args) < 2:
            print(INST_ID_MISSING)
        elif "{}.{}".format(args[0], args[1]) not in all_obj:
            print(INST_NOT_FOUND)
        else:
            print(all_obj["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        all_obj = storage.all()
        args = custom_parser(arg)
        if len(args) == 0:
            print(CLASS_NAME_MISSING)
        elif args[0] not in classes:
            print(NO_CLASS)
        elif len(args) < 2:
            print(INST_ID_MISSING)
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
        all_obj = storage.all()
        args = custom_parser(arg)

        if len(args) == 0:
            print(CLASS_NAME_MISSING)
            return

        class_name = args[0]
        if class_name not in classes:
            print(NO_CLASS)
            return

        if len(args) == 1:
            print(INST_ID_MISSING)
            return

        instance_id = f"{class_name}.{args[1]}"
        if instance_id not in all_obj.keys():
            print(INST_NOT_FOUND)
            return

        if len(args) == 2:
            print(ATTR_NAME_MISSING)
            return

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print(ATTR_VALUE_MISSING)
                return

        obj = all_obj[instance_id]
        attr_name = args[2]
        if len(args) == 4:
            attr_value = args[3]
            if attr_name in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[attr_name])
                obj.__dict__[attr_name] = val_type(attr_value)
            else:
                obj.__dict__[attr_name] = attr_value
        else:
            for key, value in eval(attr_name).items():
                if key in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[key]) in {str, int, float}:
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)
                else:
                    obj.__dict__[key] = value

        storage.save()

    def emptyline(self):
        """Does not execute anything"""
        pass

    def do_count(self, arg):
        """Retrieves the number of instances of a class."""
        args = custom_parser(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """
        Called when the command prefix is not recognized
        """

        command_mapping = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        args = arg.split('.', 1)
        if len(args) == 2:
            search = re.search(r"\((.*?)\)", args[1])
            if search:
                command = [args[1][:search.span()[0]], search.group()[1:-1]]
                if command[0] in command_mapping.keys():
                    call = f"{args[0]} {command[1]}"
                    return command_mapping[command[0]](call)

        print(f"*** Unknown syntax: {arg}")


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
