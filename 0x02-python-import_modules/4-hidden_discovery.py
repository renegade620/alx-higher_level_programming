#!/usr/bin/python3

if __name_ == "__main_":

    import hidden_4

    ns = dir(hidden_4)
    for name in ns:
        if name[:2] != "__":
            print(name)
