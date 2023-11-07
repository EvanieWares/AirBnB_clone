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


PROMPT = '(hbnb) '
MISSING_CLASS_NAME = '** class name missing **'
NO_CLASS = "** class doesn't exist **"
MISSING_INST_ID = '** instance id missing **'
INST_NOT_FOUND = '** no instance found **'


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
        pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        pass

    def emptyline(self):
        """Does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
