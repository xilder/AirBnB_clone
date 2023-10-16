#!/usr/bin/python3
"""
defines the console for the AirBnB clone
"""
import cmd
import json
import re
from shlex import split as split_line
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defines the class commands for the console

    Type "help" to display the list of available
    commands

    Type "help <command>" to get help on how to use
    <command>

    Attributes:

        prompt: console prompt
        __classes: list of class models
    """

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Place", "State",
                 "City", "Amenity", "Review"]

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
        print("This command allows you to exit the  interpreter", end=" ")
        print("cleanly by pressing the Ctrl Key + D key")

    def emptyline(self):
        """
        Skips any empty line command
        """

        pass

    def validate_line(self, line, flag):
        """
        Validates every line based on the input

        Args:
            line (str): line to be validated
            flag (int): determines the kind of validation to use
                1. validates for the create method
                2. validates for the show method
        """

        line_arg = split_line(line)

        if flag >= 1 and len(line_arg) == 0:
            print("** class name missing **")
        elif flag >= 1 and line_arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif flag >= 2 and len(line_arg) == 1:
            print("** instance id missing **")
        else:
            return line_arg
        return False

    def do_create(self, line):
        """
        Creates an instance of a class if it exists and saves it to storage

        Args:
            line (str): User input containing the class instance to be created
        """

        line_arg = self.validate_line(line, 1)

        if line_arg:
            new_model = eval(line_arg[0])()
            new_model.save()
            print(new_model.id)

    def help_create(self):
        """
        Help for the create command
        """

        print("\nUsage: create <model_class>")
        print("This command creates an instance of the specified", end=" ")
        print("class and assigns it a unique identifier")
        print("Finally, it prints the instance's id")

    def do_show(self, line):
        """
        Displays the string representation of an instance

        Args:
            line (str): User input containing the class instance and id
                        to be displayed
        """

        line_arg = self.validate_line(line, 2)

        if line_arg:
            all_instances = storage.all()
            instance = f"{line_arg[0]}.{line_arg[1]}"

            if instance in all_instances:
                print(all_instances[instance])
            else:
                print("** no instance found **")

    def help_show(self):
        """
        Help for the show method
        """

        print("\nUsage: show <model_class> <model_id>")
        print("This command displays the string representation", end=" ")
        print("of an instance if the id provided exists")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id given

        Args:
            line (str): User inout containing the class instance and id
                        to be destroyed
        """

        line_arg = self.validate_line(line, 2)

        if line_arg:
            all_instances = storage.all()
            instance = f"{line_arg[0]}.{line_arg[1]}"

            if instance in all_instances:
                del all_instances[instance]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """
        Help for the destroy method
        """

        print("\nUsage: destroy <model_class> <model_id>")
        print("This command deletes an instance based on the", end=" ")
        print("class name and id if they exist in the storage")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class

        Args:

            line: if present, specifies the model instances to be
                else prints all available instances
        """

        if line and line not in self.__classes:
            print("** class doesn't exist **")
        else:
            all_instances = storage.all()
            class_instances = []

            for k, v in all_instances.items():
                if line:
                    if line == v.to_dict()["__class__"]:
                        class_instances.append(str(v))
                else:
                    class_instances.append(str(v))
            print(class_instances)

    def help_all(self):
        """
        Help for the all method
        """

        print("\nUsage 1: all")
        print("This prints all instances in storage")
        print("\nUsage 2: all <model_class>")
        print("This prints all instances of the provided", end=" ")
        print("<model_class>")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attritbute and saves the changes into the JSON file

        Args:

            line: user input specifying the exact instance and
            instance's attribute to be updated
        """

        line_arg = self.validate_line(line, 2)
        if line_arg:
            all_instances = storage.all()
            instance = f"{line_arg[0]}.{line_arg[1]}"

            if instance not in all_instances:
                print("** no instance found **")
            elif len(line_arg) == 2:
                print("** attribute name missing **")
            elif len(line_arg) == 3:
                print("** value missing **")
            else:
                instance = all_instances[instance]
                attr, val = line_arg[2], line_arg[3]
                if attr in ["number_rooms",
                         "number_bathrooms",
                         "max_guest",
                         "price_by_night"]:
                    val = int(val)
                elif attr in ["latitude",
                           "longitude"]:
                    val = float(val)
                setattr(instance, attr, val)
                instance.save()

    def help_update(self):
        """
        Help for the update method
        """

        print("\nUsage: update <model_class>", end=" ")
        print("<model_id> <attribute> <value>")
        print("This command updates an instance's", end=" ")
        print("attribute with the given value")

    def do_update2(self, line):
        """
        Updates an instance based on the class name and id with a given
        dictionary and saves the changes into the JSON file

        Args:
            line (str): contains the class and id
            dict_val (dict): dictionary of values to update the instance
        """

        new_args = line.split(" {", 1)
        line_arg = new_args[0]
        dict_vals = "{" + new_args[1]
        dict_vals = json.loads(dict_vals)
        line_arg = self.validate_line(line, 2)
        if line_arg:
            all_instances = storage.all()
            instance = f"{line_arg[0]}.{line_arg[1]}"
            if instance not in all_instances:
                print("** no instance found **")
            else:
                instance = all_instances[instance]
                for k, v in dict_vals.items():
                    if k in ["number_rooms",
                             "number_bathrooms",
                             "max_guest",
                             "price_by_night"]:
                        v = int(v)
                    elif k in ["latitude",
                               "longitude"]:
                        v = float(v)
                    setattr(instance, k, v)
                instance.save()

    def do_count(self, line):
        """
        Prints all string representation of all instances based
        or not on the class
        Args:
            line: if present, orints number of the specified model instances
                else prints the total number of instances
        """
        if line and line not in self.__classes:
            print("** class doesn't exist **")
        else:
            all_instances = storage.all()
            number_of_instances = 0
            for v in all_instances.values():
                if line:
                    if line == v.to_dict()["__class__"]:
                        number_of_instances += 1
                else:
                    number_of_instances += 1
            print(number_of_instances)

    def help_count(self):
        """
        Help for the count method
        """
        print("\nUsage 1: count")
        print("This prints the numbe of  instances in storage")
        print("\nUsage 2: count <model_class>")
        print("This prints the number of instance of the provided", end=" ")
        print("<model_class>")

    def default(self, line):
        """
        Handles commands for the format class.<command>.(<additional args>)
        and any other default command

        Args:
            line (str): user input string
        """
        method_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        matches = re.match(r"(\w+)\.(\w+)\((.*)\)", line)
        if matches:
            class_name = str(matches.group(1))
            method_name = str(matches.group(2))
            added_args = str(matches.group(3))
            added_args = added_args.split(", ", 1)
            line = f"{class_name}"
        else:
            method_name = ""

        if matches and method_name in ["all", "count"]:
            method_dict[method_name](line)
        elif method_name in ["show", "destroy"]:
            try:
                instance_id = added_args[0]
                line = f"{line} {instance_id}"
                method_dict[method_name](line)
            except IndexError:
                line = ""
                method_dict[method_name](line)
        elif method_name == "update":
            try:
                instance_id = added_args[0]
                attr_params = added_args[1]
                if attr_params[0] != "{":
                    attr_params = attr_params.replace(",", "")
                    line = f"{line} {instance_id} {attr_params}"
                    method_dict[method_name](line)
                else:
                    attr_params = attr_params.replace("\'", "\"")
                    line = f"{line} {instance_id} {attr_params}"
                    self.do_update2(line)
            except IndexError:
                line = ""
                method_dict[method_name](line)
        else:
            super().default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
