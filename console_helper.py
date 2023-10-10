#!/usr/bin/env python3

"""Defines HBNBCommandHelper, which provides methods to,execute commands."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommandHelper:
    """This class provides methods to execute various commands."""

    class_mapping = {
        'BaseModel': BaseModel,
        # 'User': User,
        # 'City': City,
        # 'Place': Place,
        # 'Amenity': Amenity,
        # 'Review': Review,
        # 'State': State
    }

    @staticmethod
    def execute_command(command_name, args):
        """
        Execute the given command with the provided arguments.

        Args:
            command_name (str): The name of the command to execute.
            args (list): List of arguments for the command.
        """
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
        else:
            print(f"Unknown command: {command_name}")

    @staticmethod
    def do_create(args):
        """
        Execute the 'create' command.

        Args:
            args (list): List of arguments for the 'create' command.
        """
        # get class name
        class_name = args[0]

        # create the object
        obj = HBNBCommandHelper.class_mapping[class_name]()

        # save object to file storage
        FileStorage.new(obj)
        FileStorage.save()

        print("{} created with id {}".format(class_name, obj.id))

    @ staticmethod
    def do_show(args):
        """
        Execute the 'show' command.

        Args:
            args (list): List of arguments for the 'show' command.
        """
        if not HBNBCommandHelper.isvalid_args(args):
            return
        if not HBNBCommandHelper.isvalid_key(args):
            return

        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = FileStorage.all()

        class_obj = HBNBCommandHelper.class_mapping[class_name](
            **objects.get(key))
        print(str(class_obj))

    @ staticmethod
    def do_destroy(args):
        """
        Execute the 'destroy' command.

        Args:
            args (list): List of arguments for the 'destroy' command.
        """
        if not HBNBCommandHelper.isvalid_args(args) or \
                not HBNBCommandHelper.isvalid_key(args):
            return

        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = FileStorage.all()

        del objects[key]
        FileStorage.save()

    @ staticmethod
    def do_all(args):
        """
        Execute the 'all' command.

        Args:
            args (list): List of arguments for the 'all' command.
        """
        objects = FileStorage.all()

        if not args:
            return HBNBCommandHelper.print_all_no_args(args, objects)
        else:
            return HBNBCommandHelper.print_all_from_args(args, objects)

    @staticmethod
    def print_all_from_args(args, objects):
        """Print all objects when no args are specified."""
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
        """Print all objects when no args are specified."""
        result_list = []
        for key, val in objects.items():
            parsed_class_name = key.split(".")[0]

            if parsed_class_name not in HBNBCommandHelper.class_mapping:
                print("** class doesn't exist **")
                continue

            class_ctor = HBNBCommandHelper.class_mapping[parsed_class_name]
            result_list.append(str(class_ctor(**val)))
        print(result_list)
        return

    @ staticmethod
    def do_update(args):
        """
        Execute the 'update' command.

        Args:
            args (list): List of arguments for the 'update' command.
        """
        if not HBNBCommandHelper.isvalid_args(args) or \
                not HBNBCommandHelper.isvalid_key(args):
            return
        print('Executing update logic with args:', args)

    @ staticmethod
    def isvalid_class_name(args):
        """Determine if class name exists or is not specified."""
        if (args == []):
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in HBNBCommandHelper.class_mapping:
            print("** class doesn't exist **")
            return False

        # Return true ottherwise
        return True

    def isvalid_args(args):
        """Check if the recieved args are valid."""
        # create key of object in storage
        if not isinstance(args, list):
            return False

        if list.__len__(args) != 2:
            print("** instance id missing **")
            return False

        return True

    def isvalid_key(args):
        """Check if parsed key is existing or valid."""
        # create key and get all objects
        class_name, obj_id = args[0], args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = FileStorage.all()

        # look for requested object
        if key not in objects.keys():
            print("** no instance found **")
            return False

        return True
