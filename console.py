"""
console.py - A Python program implementing a command interpreter using the cmd module.

This program defines the HBNBCommand class, which inherits from cmd.Cmd and provides a command interpreter
with specific features, including a custom prompt, handling quit and EOF commands, displaying help, and more.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements a command interpreter using the cmd module.
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """
        Overrides the default behavior to do nothing for an empty line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit the program.
        """
        exit()

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to quit the program.
        """
        print('')
        exit()

    def do_help(self, arg):
        """
        Display help for available commands.
        """
        help_info = {'quit': 'This command quits the program.',
                     'EOF': 'This command quits the program.',
                     'help': 'Display help for available commands'}

        if arg in help_info.keys():
            print(help_info[arg])
        else:
            commands = help_info.keys()
            formatted_string = "Documented commands (type help <topic>):\n========================================\n{}\n".format("  ".join(commands))
            print(formatted_string)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
