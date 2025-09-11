def check_lists(list1, list2):
    if list1 == list2:
        return EQUAL
    list1 = '-'.join(str(char) for char in list1)
    list2 = '-'.join(str(char) for char in list2)
    if list1 in list2:
        return SUBLIST
    if list2 in list1:
        return SUPERLIST
    return UNEQUAL

def EQUAL():
    pass

def UNEQUAL():
    pass

def SUBLIST():
    pass

def SUPERLIST():
    pass
