# q4
#a

from DoublyLinkedList import *

class Empty(Exception):
    pass

def copy_linked_list(lnk_lst):
    copy = DoublyLinkedList()

    for i in lnk_lst:
        copy.add_last(i)

    return copy

#b

def deep_copy_linked_list(lnk_lst):
    copy = DoublyLinkedList()

    for i in lnk_lst:
        if type(i) == int:
            copy.add_last(i)
        else:
            copy.add_last(deep_copy_linked_list(i))

    return copy