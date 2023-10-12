#!/usr/bin/python3
"""
defines the console for the AirBnB clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines the class commands for the console

    Type "help" to display the list of available
    commands

    Type "help <command>" to get help on how to use
    <command>
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exits the interpreter cleanly
        """
        return True

    def help_quit(self):
        """
        Provides help information on the quit command
        """
        print("\nUsage: quit\n")
        print("This command allows you to exit the interpreter", end=" ")
        print("cleanly")

    def do_EOF(self, line):
        """
        Exits the interpreter cleanly
        """
        return True

    def help_EOF(self):
        """
        Provides help information on the EOF command
        """
        print("\nUsage: EOF\n")
        print("This command allos you to exit the  interpreter", end=" ")
        print("cleanly by pressing the Ctrl Key + D key")

    def emptyline(self):
        """
        Skips any empty line command
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
