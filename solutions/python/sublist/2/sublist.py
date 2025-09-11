UNEQUAL, SUBLIST, SUPERLIST, EQUAL  = "NE", "SUB", "SUP", "EQ"

def check_lists(list1, list2):

    def is_sub(list1, list2):
        len1, len2 = len(list1), len(list2)
        return any(
            list2[pos:pos+len1] == list1 for pos in range(len2)
            )

    return(
        EQUAL if list1 == list2
        else SUBLIST if is_sub(list1, list2)
        else SUPERLIST if is_sub(list2, list1)
        else UNEQUAL
        )

