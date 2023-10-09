#!/bin/usr/env pyython3

"""Defines HBNBCommandHelper, which provides methods to,execute commands."""


class HBNBCommandHelper:
    """This class provides methods to execute various commands."""

    @staticmethod
    def execute_command(command_name, args):
        """
        Execute the given command with the provided arguments.

        Args:
            command_name (str): The name of the command to execute.
            args (list): List of arguments for the command.
        """
        if command_name == 'create':
            HBNBCommandHelper.do_create(args)
        elif command_name == 'show':
            HBNBCommandHelper.do_show(args)
        elif command_name == 'destroy':
            HBNBCommandHelper.do_destroy(args)
        elif command_name == 'all':
            HBNBCommandHelper.do_all(args)
        elif command_name == 'update':
            HBNBCommandHelper.do_update(args)
        else:
            print(f"Unknown command: {command_name}")

    @staticmethod
    def do_create(args):
        """
        Execute the 'create' command.

        Args:
            args (list): List of arguments for the 'create' command.
        """
        print('Executing create logic with args:', args)

    @staticmethod
    def do_show(args):
        """
        Execute the 'show' command.

        Args:
            args (list): List of arguments for the 'show' command.
        """
        print('Executing show logic with args:', args)

    @staticmethod
    def do_destroy(args):
        """
        Execute the 'destroy' command.

        Args:
            args (list): List of arguments for the 'destroy' command.
        """
        print('Executing destroy logic with args:', args)

    @staticmethod
    def do_all(args):
        """
        Execute the 'all' command.

        Args:
            args (list): List of arguments for the 'all' command.
        """
        print('Executing all logic with args:', args)

    @staticmethod
    def do_update(args):
        """
        Execute the 'update' command.

        Args:
            args (list): List of arguments for the 'update' command.
        """
        print('Executing update logic with args:', args)
