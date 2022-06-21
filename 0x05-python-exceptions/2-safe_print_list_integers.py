#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    counter = 0
    
    while n < x:
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
            pass
         else:
            counter += 1
        finally:
            i += 1
    print()
    return count
