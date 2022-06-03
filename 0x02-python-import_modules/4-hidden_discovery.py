#!/usr/bin/python3

if _name_ == "_main_":

    import hidden_4

    ns = dir(hidden_4)
    for name in ns:
        if name[:2] != "__":
            print(name)
