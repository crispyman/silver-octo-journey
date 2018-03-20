#!/usr/bin/env python3
# coding=utf-8
import random


def bogosort(input_list):
    """
    :param input_list: a list of unicode characters and/or numbers.
    :return output_list: an ordered list of characters/numbers.
    """
    # pseudo random number generator appears to be time based, list would repeat in same order multiple times.
    random.SystemRandom()
    output_list = []
    if not input_list:
        return False
    is_ordered_list = False
    while not is_ordered_list:
        input_copy = list(input_list)
        output_list.append([])

        while len(input_copy) > 0:
            output_list[-1].append(str(input_copy.pop(random.randrange(len(input_copy)))))
        old__value = ""
        for value in output_list[-1]:
            if value > old__value:
                is_ordered_list = True
                old__value = value
            else:
                is_ordered_list = False
                break
    return output_list

if __name__ == "__main__":
	print(bogosort(['a', 'b', 'c']))

