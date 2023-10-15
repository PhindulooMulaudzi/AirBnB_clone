#!/usr/bin/python3

"""
Defines HBNBCommandHelper, which provides methods to execute commands.

This module defines the HBNBCommandHelper class, which offers methods to
execute various commands related to the AirBnB clone project. It includes
commands such as create, show, destroy, update, and all, allowing manipulation
of instances and their attributes.

Attributes:
    class_mapping (dict): Mapping of class names to their corresponding
                         class objects (e.g., 'BaseModel': BaseModel).

"""

import re
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.review import Review
from models.user import User


class HBNBCommandHelper:
    """This class provides methods to execute various commands.

    The HBNBCommandHelper class contains static methods to
    execute different commands related to the AirBnB clone project.
    It uses a class_mapping dictionary to map command names to
    their respective classes.

    Attributes:
        class_mapping (dict): A mapping of command names to their respective
        class objects.
        registered_commands (list): A list of registered command names.
    """

    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    registered_commands = ["all", "create", "show", "destroy", "update"]

    @ staticmethod
    def handle_class_based_commands(command_name, args):
        """Handle class based commands like User.all().

        Args:
            User input args, with command name

        Returns:
            command_name and args.
        """
        split_string = command_name.split('.')

        if len(split_string) < 2:
            return None, None

        class_name = split_string[0]
        split_args = split_string[1].split('(')

        if len(split_args) < 2:
            return None, None

        cmd = split_args[0]
        arg1 = split_args[1][:-1]

        if arg1.startswith('"') and \
                arg1.endswith('"'):
            arg1 = arg1[1:-1]

        if args is None:
            args = [str(class_name), str(arg1)]
        else:
            args_list = []
            args_list.extend([class_name, str(arg1)])
            for arg in args:
                iarg = re.sub(r'[^a-zA-Z0-9]', '', arg)
                args_list.append(iarg)

        command_name = str(cmd)

        return command_name, args_list

    @staticmethod
    def execute_command(command_name, args):
        """Execute the given command with the provided arguments.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        class_cmd, class_args = \
            HBNBCommandHelper.handle_class_based_commands(command_name, args)
        if class_cmd and class_args:
            command_name = class_cmd
            args = class_args

        if command_name not in HBNBCommandHelper.registered_commands:
            print(f"Unknown command: {command_name}")
            return

        if command_name == 'all':
            HBNBCommandHelper.do_all(args)
            return
        if not HBNBCommandHelper.isvalid_class_name(args):
            return
        if command_name == 'create':
            HBNBCommandHelper.do_create(args)
        elif command_name == 'show':
            HBNBCommandHelper.do_show(args)
        elif command_name == 'destroy':
            HBNBCommandHelper.do_destroy(args)
        elif command_name == 'update':
            HBNBCommandHelper.do_update(args)

    @staticmethod
    def do_create(args):
        """Execute the 'create' command.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        # get class name
        class_name = args[0]

        # create the object
        obj = HBNBCommandHelper.class_mapping[class_name]()

        # save object to file storage
        obj.save()

        print(obj.id)

    @ staticmethod
    def do_show(args):
        """Execute the 'show' command.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        if not HBNBCommandHelper.isvalid_args(args):
            return
        if not HBNBCommandHelper.isvalid_key(args):
            return

        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        class_obj = HBNBCommandHelper.class_mapping[class_name](
            **objects.get(key))
        print(str(class_obj))

    @ staticmethod
    def do_destroy(args):
        """Execute the 'destroy' command.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        if not HBNBCommandHelper.isvalid_args(args) or \
                not HBNBCommandHelper.isvalid_key(args):
            return

        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        del objects[key]
        storage.save()

    @ staticmethod
    def do_all(args):
        """Execute the 'all' command.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        objects = storage.all()

        if not args:
            return HBNBCommandHelper.print_all_no_args(args, objects)
        else:
            return HBNBCommandHelper.print_all_from_args(args, objects)

    @staticmethod
    def print_all_from_args(args, objects):
        """Print all objects when no args are specified.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        class_name = args[0]
        if class_name not in HBNBCommandHelper.class_mapping:
            print("** class doesn't exist **")
            return

        result_list = []
        for key, val in objects.items():
            parsed_class_name = str.split(key, ".")[0]

            if parsed_class_name != class_name:
                continue

            class_obj = HBNBCommandHelper.class_mapping[parsed_class_name](
                **val)
            result_list.append(str(class_obj))
        print(result_list)
        return

    @staticmethod
    def print_all_no_args(args, objects):
        """Print all objects when no args are specified.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        result_list = []
        for key, val in objects.items():
            parsed_class_name = key.split(".")[0]

            if parsed_class_name not in HBNBCommandHelper.class_mapping:
                # print("** class doesn't exist **")
                continue

            class_ctor = HBNBCommandHelper.class_mapping[parsed_class_name]
            result_list.append(str(class_ctor(**val)))
        print(result_list)
        return

    @ staticmethod
    def do_update(args):
        """Execute the 'update' command.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            None
        """
        if not HBNBCommandHelper.isvalid_args(args) or \
                not HBNBCommandHelper.isvalid_key(args)\
                or not HBNBCommandHelper.isvalid_attributes(args):
            return

        class_name, obj_id = args[0], args[1]
        attribute, attr_value = args[2], args[3]
        illegal_attributes = ["id", "created_at", "updated_at"]

        # strip quotes from string attribute value
        if isinstance(attr_value, str) and \
            attr_value.startswith('"') and \
                attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        if attribute in illegal_attributes:
            print("Illegal attribute update attempted")
            return

        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        objects[key][attribute] = attr_value

        class_obj = HBNBCommandHelper\
            .class_mapping[class_name](**objects[key])
        class_obj.save()

    @ staticmethod
    def isvalid_attributes(args):
        """Check if attributes passed in as arguments are valid.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            True if valid, False otherwise.
        """
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        if len(args) == 4:
            return True

        return False

    @ staticmethod
    def isvalid_class_name(args):
        """Determine if class name exists or is not specified.

        Args:
            args (list): The arguments for the command.

        Returns:
            True if valid, False otherwise.
        """
        if (args == []):
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in HBNBCommandHelper.class_mapping:
            print("** class doesn't exist **")
            return False

        # Return true ottherwise
        return True

    @staticmethod
    def isvalid_args(args):
        """Check if the recieved args are valid.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            True if valid, False otherwise.
        """
        # create key of object in storage
        if not isinstance(args, list):
            return False

        if list.__len__(args) < 2:
            print("** instance id missing **")
            return False

        return True

    @staticmethod
    def isvalid_key(args):
        """Check if parsed key is existing or valid.

        Args:
            command_name (str): The name of the command to execute.
            args (list): The arguments for the command.

        Returns:
            True if valid, False otherwise.
        """
        # create key and get all objects
        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        # look for requested object
        if key not in objects.keys():
            print("** no instance found **")
            return False

        return True
