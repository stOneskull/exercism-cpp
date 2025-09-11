EQUAL, UNEQUAL, SUBLIST, SUPERLIST = range(4)

def check_lists(list1, list2):
    return (
        EQUAL if list1 == list2
        else SUBLIST if is_sub(list1, list2)
        else SUPERLIST if is_sub(list2, list1)
        else UNEQUAL
    )
    
def is_sub(lace, yarn):
    knots, line = len(lace), len(yarn)  
    return any(
        yarn[knot:knot+knots] == lace 
        for knot in range(line)
    )


