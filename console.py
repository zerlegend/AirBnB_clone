#!/usr/bin/env python3
"""This module defines the HBNB command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Handles emptyline + ENTER input."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
