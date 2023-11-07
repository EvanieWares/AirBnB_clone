#!/usr/bin/python3
"""
Implements a class which act as the entry point of command interpreter.

The class obey the following conventions:

1. End of file on input exits the command interpreter
2. A command 'quit' exits the program

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter which inherits from cmd module
    """
    prompt = '(hbnb) '

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

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
