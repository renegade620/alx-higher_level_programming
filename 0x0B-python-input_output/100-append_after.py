#!/usr/bin/python3
"""  Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.readlines()
        new_text = []

        for line in text:
            new_text.append(line)

            if search_string in line:
                new_text.append(new_string)

    with open(filename, "w", encoding="utf-8") as fn:
        for line in new_text:
            fn.write(line)
