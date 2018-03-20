#!/usr/bin/env python3
# coding=utf-8
"""
BogoSort class.
"""
__author__ = "That guy"
__version__ = "I hope a string here breaks someones something but I doubt it will"

# I need some better naming conventions or else I need to make everything impossible to read
from bogosort import bogosort as bogo

class BogoSort:
    """
    Does almost useless bogosort stuff.
    Now with deduplication.
    TODO: Unit tests
    """

    def __init__(self, input_list):
        self.__list_of_list = BogoSort.sort(input_list)

    def print_list(self):
        """
        :return: returns the list.
        """
        return self.__list_of_list

    @staticmethod
    def sort(input_list):

        """
        :param input_list: a list of unicode characters and/or numbers.
        :return output_list: an ordered list of characters/numbers.
        """
        return bogo(input_list)

    def dedupe_list(self):
        """
        :return: returns a deduplicated list of lists.
        """
        sub_list1, sub_list2 = 0, 0
        copy = list(self.__list_of_list)
        while sub_list1 < len(copy):
            while sub_list2 < len(copy):
                if sub_list1 == sub_list2:
                    pass
                elif copy[sub_list1] == copy[sub_list2]:
                    copy.pop(sub_list2)
                sub_list2 += 1
            sub_list2 = 0
            sub_list1 += 1
        return copy


if __name__ == "__main__":
    b = BogoSort(['a', 'b', 'c'])
    print(b.print_list())
    print(b.dedupe_list())
