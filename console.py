#!/usr/bin/env python3

"""console.py - A Python program implementing a command interpreter."""

import cmd
from console_helper import HBNBCommandHelper


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class implements a command interpreter."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Override the default behavior to do nothing for an empty line."""
        pass

    def do_quit(self, arg):
        """Quit the program."""
        exit()

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to quit the program."""
        print('')
        exit()

    def do_help(self, arg):
        """Display help for available commands."""
        help_info = {
            'quit': 'This command quits the program.',
            'EOF': 'This command quits the program.',
            'help': 'Display help for available commands.',
            'create': 'Creates a new instance of BaseModel.',
            'show': 'Prints the string representation of an instance.',
            'destroy': 'Prints the string representation of an instance.',
            'all': 'Prints all string representation of all instances.',
            'update': 'Prints all string representation of all instances.',
        }

        if arg in help_info.keys():
            print(help_info[arg])
        else:
            commands = help_info.keys()
            formatted_string = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "{}\n".format("  ".join(commands))
            )
            print(formatted_string)

    def do_command(self, args):
        """Execute a command using HBNBCommandHelper."""
        command_name, *command_args = args.split()
        HBNBCommandHelper.execute_command(command_name, command_args)

    def default(self, line):
        """Override default method to call do_command for any input."""
        self.do_command(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
