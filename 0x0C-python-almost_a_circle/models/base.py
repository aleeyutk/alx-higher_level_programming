#!/usr/bin/python3
"""
Base
"""
import json
import os


class Base:
    """
    Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for
        sharing data representation
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        adding the class method def save_to_file(cls, list_objs):
        that writes the JSON string representation of list_objs to a
        file
        """
        nfile = "{}.json".format(cls.__name__)
        nlist = []

        if list_objs is not None:
            for i in list_objs:
                nlist.append(cls.to_dictionary(i))

        with open(nfile, mode="w", encoding='utf-8') as f:
            f.write(cls.to_json_string(nlist))

    @staticmethod
    def from_json_string(json_string):
        """
        adding the static method def from_json_string(json_string):
        that returns the list of the JSON string
        representation json_string
        """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        adding the class method def create(cls, **dictionary):
        that returns an instance with all attributes already set
        """

        if cls.__name__ == "Square":
            dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        adding the class method def load_from_file(cls):
        that returns a list of instances
        """

        nfile = "{}.json".format(cls.__name__)
        listsq = []

        if os.path.isfile(nfile):
            with open(nfile, encoding="utf-8") as f:
                items = cls.from_json_string(f.read())
            for i in items:
                listsq.append(cls.create(**i))
            return listsq
        else:
            return []
