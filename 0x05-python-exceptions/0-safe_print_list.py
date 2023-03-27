#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    r_num = 0
    for i in my_list:
        for i in range(x):
            try:
                print(my_list[i], end="")
                r_num += 1
